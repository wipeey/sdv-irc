const input = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');
const chatMessages = document.getElementById('chat'); // Ajoutez cet élément à votre HTML

// Créer une connexion WebSocket vers le serveur
const websocket = new WebSocket('ws://172.232.43.133:8080');

function sendMessage() {
    const message = input.value.trim();
    if (message && websocket.readyState === WebSocket.OPEN) {
        websocket.send(message);
        displayMessage('Vous', message); // Affiche le message localement
        input.value = '';
    }
}

function displayMessage(sender, message) {
    const messageElement = document.createElement('div');
    console.log(`${sender}: ${message}`);
    //chatMessages.appendChild(messageElement);
    //chatMessages.scrollTop = chatMessages.scrollHeight; // Défilement automatique
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

