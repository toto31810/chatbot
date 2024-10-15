document.addEventListener('DOMContentLoaded', function() {
    const chatIcon = document.getElementById('chatIcon');
    const chatContainer = document.getElementById('chatContainer');
    const closeBtn = document.getElementById('closeBtn');
    const chatInput = document.getElementById('user-input');

    chatIcon.addEventListener('click', function() {
        chatContainer.style.display = chatContainer.style.display === 'block' ? 'none' : 'block';
        if (chatContainer.style.display === 'block') {
            displayPredefinedQuestions();
        }
    });

    closeBtn.addEventListener('click', function() {
        chatContainer.style.display = 'none';
    });

    chatInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});

// Questions prédéfinies
const predefinedQuestions = [
    "Comment réinitialiser mon mot de passe ?",
    "Quels sont les tarifs des services ?",
    "Comment contacter le support ?"
];

function displayPredefinedQuestions() {
    const questionContainer = document.getElementById('predefined-questions');
    questionContainer.innerHTML = ''; // Nettoyer les anciennes questions

    predefinedQuestions.forEach(question => {
        const questionButton = document.createElement('button');
        questionButton.className = 'predefined-question';
        questionButton.textContent = question;
        questionButton.onclick = () => handlePredefinedQuestion(question);
        questionContainer.appendChild(questionButton);
    });
}

function handlePredefinedQuestion(question) {
    document.getElementById('user-input').value = question;
    sendMessage();
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    const chatBox = document.getElementById('chat-box');
    const userMessage = document.createElement('div');
    userMessage.className = 'message user';
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    const loadingMessage = document.createElement('div');
    loadingMessage.className = 'message bot loading';
    loadingMessage.textContent = 'Chargement...';
    chatBox.appendChild(loadingMessage);

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.removeChild(loadingMessage);
        const botMessage = document.createElement('div');
        botMessage.className = 'message bot';
        botMessage.textContent = data.response || "Désolé, je n'ai pas pu générer de réponse.";
        chatBox.appendChild(botMessage);
    })
    .catch(error => {
        chatBox.removeChild(loadingMessage);
        console.error('Error:', error);
        const botMessage = document.createElement('div');
        botMessage.className = 'message bot';
        botMessage.textContent = "Désolé, une erreur s'est produite.";
        chatBox.appendChild(botMessage);
    });

    document.getElementById('user-input').value = '';
    chatBox.scrollTop = chatBox.scrollHeight;
}
