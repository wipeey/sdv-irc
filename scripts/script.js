document.addEventListener("DOMContentLoaded", function() {
    const scrollingContent = document.getElementById('scrollingContent');
    const clone = scrollingContent.cloneNode(true); // Clone le contenu
    scrollingContent.parentElement.appendChild(clone); // Ajoute le clone à la suite pour un effet continu
});

const input = document.getElementById('messageInput');
const chatMessages = document.getElementById('chat');

function sendMessage(message){
    const messageElement = document.createElement('p');
    messageElement.textContent = `${sender}: ${message}`;
    chatMessages.appendChild(messageElement);
}
document.addEventListener("DOMContentLoaded", sendMessage)