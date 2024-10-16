from flask import Flask, request, jsonify, render_template
import requests
import json
import os

app = Flask(__name__)

# URL API Rasa
RASA_URL = 'http://localhost:5005/webhooks/rest/webhook'  

# base de connaissances
knowledge_base_path = os.path.join('data', 'knowledge_base.json')
try:
    with open(knowledge_base_path, 'r') as file:
        knowledge_base = json.load(file)
except FileNotFoundError:
    knowledge_base = {}
    print(f"Le fichier {knowledge_base_path} n'a pas été trouvé.")

def get_response_from_rasa(user_input):
    data = {
        'sender': 'user',  # Identifiant de l'utilisateur
        'message': user_input  # Message de l'utilisateur
    }
    
    try:
        response = requests.post(RASA_URL, json=data)
        response.raise_for_status()  # Vérifie si la requête a réussi
        return response.json()  # Retourne la réponse de Rasa
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API Rasa: {e}")
        return {'error': 'Erreur lors de l\'appel à l\'API Rasa'}

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response_from_rasa(user_input)

    if 'error' in response:
        return jsonify(response), 500  # Retourne une erreur en cas de problème

    return jsonify(response)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
