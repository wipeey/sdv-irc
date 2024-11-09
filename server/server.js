const WebSocket = require('ws');

// Créer un serveur WebSocket sur le port 8080
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
    console.log('Un client est connecté');

    // Écoute les messages du client
    ws.on('message', (message) => {
        console.log(`Message reçu : ${message}`);

        // Envoie le même message à tous les clients connectés
        wss.clients.forEach(client => {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(message);
            }
        });
    });

    // Envoie un message d'accueil au nouveau client
    ws.send('Bienvenue dans le chat!');
});
