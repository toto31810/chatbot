document.addEventListener('DOMContentLoaded', function() {
    const chatIcon = document.getElementById('chatIcon');
    const chatContainer = document.getElementById('chatContainer');
    const closeBtn = document.getElementById('closeBtn');

    chatIcon.addEventListener('click', function() {
        chatContainer.style.display = 'block';
    });

    closeBtn.addEventListener('click', function() {
        chatContainer.style.display = 'none';
    });
});

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
        if (data.response) {
            const botMessage = document.createElement('div');
            botMessage.className = 'message bot';
            botMessage.textContent = data.response;
            chatBox.appendChild(botMessage);
        } else if (data.choices && data.choices[0] && data.choices[0].text) {
            const botMessage = document.createElement('div');
            botMessage.className = 'message bot';
            botMessage.textContent = data.choices[0].text;
            chatBox.appendChild(botMessage);
        } else {
            const botMessage = document.createElement('div');
            botMessage.className = 'message bot';
            botMessage.textContent = "Désolé, je n'ai pas pu générer de réponse.";
            chatBox.appendChild(botMessage);
        }
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
