document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");
    const overlay = document.createElement("div");
    overlay.classList.add("overlay");
    document.body.appendChild(overlay);

    cards.forEach(card => {
        card.addEventListener("click", (event) => {
            event.stopPropagation(); // Prevents overlay from immediately closing
            card.classList.add("flipped", "enlarged");
            overlay.style.display = "block";
        });
    });

    document.addEventListener("click", (event) => {
        if (!event.target.closest(".card")) {
            cards.forEach(card => {
                card.classList.remove("flipped", "enlarged");
            });
            overlay.style.display = "none";
        }
    });
});