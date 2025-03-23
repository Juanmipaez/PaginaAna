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

document.addEventListener('DOMContentLoaded', function() {
    const heartColors = ['#ff0000', '#ff3366', '#ff6699', '#ff99cc', '#ff66b2']; // Different shades of red/pink
    const heartSizes = [15,,18, 20, 23, 25, 30, 33, 35, 38, 40, 44, 47]; // Different sizes for variety
    const heartCount = 150; // Number of hearts on screen at once
    
    function createHeart() {
      const heart = document.createElement('div');
      heart.innerHTML = '❤';
      heart.className = 'falling-heart';
      
      // Randomize heart properties
      const randomX = Math.floor(Math.random() * 100); // Random horizontal position
      const randomSize = heartSizes[Math.floor(Math.random() * heartSizes.length)];
      const randomColor = heartColors[Math.floor(Math.random() * heartColors.length)];
      const randomDuration = Math.random() * 3 + 3; // Between 3-6 seconds to fall
      const randomDelay = Math.random() * 5; // Random delay for start
      
      // Set heart styles
      heart.style.cssText = `
        position: fixed;
        color: ${randomColor};
        left: ${randomX}%;
        top: -50px;
        font-size: ${randomSize}px;
        animation: fall ${randomDuration}s linear ${randomDelay}s infinite;
        z-index: -1;
        user-select: none;
        pointer-events: none;
      `;
      
      document.body.appendChild(heart);
    }
    
    // Create hearts
    for (let i = 0; i < heartCount; i++) {
      createHeart();
    }
    
    // Add the animation keyframes to the document
    const styleSheet = document.createElement('style');
    styleSheet.textContent = `
      @keyframes fall {
        0% {
          transform: translateY(0) rotate(0deg);
          opacity: 1;
        }
        85% {
          opacity: 0.7;
        }
        100% {
          transform: translateY(${window.innerHeight}px) rotate(360deg);
          opacity: 0;
        }
      }
    `;
    document.head.appendChild(styleSheet);
  });