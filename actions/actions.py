# actions.py

import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAnswerGeneralQuestions(Action):
    def name(self) -> str:
        return "action_answer_general_questions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        
        # Récupère le message de l'utilisateur
        user_message = tracker.latest_message.get('text')

        # Appelle l'API du modèle de langage (remplacez l'URL et la clé API par les vôtres)
        try:
            response = requests.post(
                "http://localhost:5005",  # Remplace cette URL par celle de ton API
                headers={
                    "Authorization": "Bearer YOUR_API_KEY",  # Remplace YOUR_API_KEY par ta clé API
                    "Content-Type": "application/json"
                },
                json={"prompt": user_message, "max_tokens": 150}  # Ajuste les paramètres selon l'API
            )

            # Vérifie si la requête a réussi
            if response.status_code == 200:
                answer = response.json().get("generated_text", "Désolé, je n'ai pas pu trouver la réponse.")
                dispatcher.utter_message(text=answer)
            else:
                dispatcher.utter_message(text="Erreur lors de l'appel à l'API. Veuillez réessayer.")

        except Exception as e:
            dispatcher.utter_message(text="Une erreur est survenue. Veuillez réessayer.")
            print(f"Erreur : {e}")  # Pour le débogage

        return []
