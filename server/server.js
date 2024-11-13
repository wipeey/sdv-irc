const WebSocket = require('ws');

// Créer un serveur WebSocket sur le port 8080
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', (ws) => {
    console.log('Un client est connecté');

    // Écoute les messages du client
    ws.on('message', (message) => {
        console.log(`Message reçu : ${message}`);

        // Envoie le même message à tous les clients connectés, sauf à l'expéditeur
        wss.clients.forEach(client => {
            if (client !== ws && client.readyState === WebSocket.OPEN) {
                client.send(message.toString()); // Convertit le message en chaîne
            }
        });
    });

    // Envoie un message d'accueil au nouveau client
    ws.send('Bienvenue dans le chat!');

    // Gestion de la déconnexion
    ws.on('close', () => {
        console.log('Un client s\'est déconnecté');
    });
});

console.log('Serveur WebSocket démarré sur le port 8080');
