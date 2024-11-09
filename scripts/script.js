document.addEventListener("DOMContentLoaded", function() {
    const scrollingContent = document.getElementById('scrollingContent');
    const clone = scrollingContent.cloneNode(true); // Clone le contenu
    scrollingContent.parentElement.appendChild(clone); // Ajoute le clone à la suite pour un effet continu
});

// Créer une connexion WebSocket vers le serveur
const websocket = new WebSocket('ws://localhost:8080');  // Assure-toi que l'URL est correcte

// Quand la connexion est ouverte
websocket.onopen = function() {
    console.log('Connexion WebSocket ouverte');
};
