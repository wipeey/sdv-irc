const chatDiv = document.getElementById('chat');
const messageInput = document.getElementById('messageInput');
// Installation requise : npm install ws
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
    ws.on('message', (message) => {
        console.log(`Message reçu : ${message}`);
        // Réémet le message à tous les clients connectés
        wss.clients.forEach(client => {
            if (client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    });
});

// Connecte au serveur WebSocket
const socket = new WebSocket('ws://localhost:8080');

// Affiche les messages entrants
socket.onmessage = function(event) {
    const newMessage = document.createElement('p');
    newMessage.textContent = event.data;
    chatDiv.appendChild(newMessage);
};

// Envoie un message au serveur
function sendMessage() {
    const message = messageInput.value;
    if (message) {
        socket.send(message);
        messageInput.value = ''; // Vide l'input après l'envoi
    }
}