document.addEventListener("DOMContentLoaded", function() {
    const scrollingContent = document.getElementById('scrollingContent');
    const clone = scrollingContent.cloneNode(true); // Clone le contenu
    scrollingContent.parentElement.appendChild(clone); // Ajoute le clone à la suite pour un effet continu
});

