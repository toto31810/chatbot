from flask import Flask, request, jsonify, render_template
import requests
import json
import os
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# api Mistral
API_KEY = 'NmXyBN6Iv6I2295kvWTZ3Ji50UhxpDZo'
API_URL = 'https://api.mistral.ai/v1/chat'  # URL mise à jour

# base de connaissances
knowledge_base_path = os.path.join('data', 'knowledge_base.json')
try:
    with open(knowledge_base_path, 'r') as file:
        knowledge_base = json.load(file)
except FileNotFoundError:
    knowledge_base = {}
    print(f"Le fichier {knowledge_base_path} n'a pas été trouvé.")

# spacy pour le français
try:
    nlp = spacy.load('fr_core_news_sm')
except OSError as e:
    print(f"Erreur lors du chargement du modèle spaCy: {e}")
    nlp = None

def get_response_from_mistral(user_input):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'mistral-large-latest',  # Modèle spécifié
        'messages': [{'role': 'user', 'content': user_input}]  # Format de message mis à jour
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Mistral: {e}")
        return {'error': 'Erreur lors de l\'appel à l\'API Mistral'}

def get_response_from_knowledge_base(user_input):
    if not knowledge_base:
        return None

    questions = [question['question'] for question in knowledge_base['questions']]
    responses = [question['response'] for question in knowledge_base['questions']]

    vectorizer = TfidfVectorizer().fit_transform(questions + [user_input])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity([vectors[-1]], vectors[:-1])

    most_similar_index = similarity.argmax()
    if similarity[0, most_similar_index] > 0.5:
        return responses[most_similar_index]
    return None

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response_from_knowledge_base(user_input)
    
    if response:  # Si une réponse est trouvée dans la base de connaissances
        return jsonify({'response': response})
    
    # Sinon, interroger l'API Mistral
    response = get_response_from_mistral(user_input)
    return jsonify(response)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
