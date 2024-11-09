const input = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

function sendMessage() {
    const message = input.value.trim();
    if (message) {
        // Send message via WebSocket (handle this part as needed)
        console.log('Message sent:', message);

        // Clear the input after sending
        input.value = '';
    }
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




// Créer une connexion WebSocket vers le serveur
const websocket = new WebSocket('ws://localhost:8080');  // Assure-toi que l'URL est correcte

// Quand la connexion est ouverte
websocket.onopen = function() {
    console.log('Connexion WebSocket ouverte');
};
