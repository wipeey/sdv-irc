const input = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chat');
let messageLog = [];

// Créer une connexion WebSocket vers le serveur
const websocket = new WebSocket('ws://172.232.43.133:8080');

function sendMessage() {
    const message = input.value.trim();
    if (message && websocket.readyState === WebSocket.OPEN) {
        websocket.send(message);
        displayMessage('Vous', message);
        input.value = '';
    }
}

function displayMessage(sender, message) {
    //console.log(`${sender}: ${message}`);
    messageLog.push(message) // Ajoute le message aux logs
    const messageElement = document.createElement('p');
    messageElement.textContent = `${sender}: ${message}`;
    console.log(messageElement)
    chatMessages.appendChild(messageElement);
}

// Handle Enter key press
input.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        sendMessage();
    }
});

// Handle Send button click
sendButton.addEventListener('click', sendMessage);

// Quand la connexion est ouverte
websocket.onopen = function() {
    console.log('Connexion WebSocket ouverte');
    displayMessage('Système', 'Connecté au chat');
}

// Réception des messages
websocket.onmessage = function(event) {
    displayMessage('Autre', event.data);

}

// Gestion des erreurs et de la fermeture
websocket.onerror = function(error) {
    console.error('Erreur WebSocket:', error);
    displayMessage('Système', 'Erreur de connexion');
}

websocket.onclose = function() {
    console.log('Connexion WebSocket fermée');
    displayMessage('Système', 'Déconnecté du chat');
}

