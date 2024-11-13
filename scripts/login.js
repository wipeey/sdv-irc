document.addEventListener("DOMContentLoaded", () => {
    const wrapper = document.querySelector('.wrapper');
    if (wrapper) {
        // Add the 'show' class after a small delay to trigger the transition
        setTimeout(() => {
            wrapper.classList.add('show');
        }, 100); // Adjust the delay if necessary
    }
});
