document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll(".card");
    const overlay = document.createElement("div");
    overlay.classList.add("overlay");
    document.body.appendChild(overlay);

    cards.forEach(card => {
        card.addEventListener("click", (event) => {
            event.stopPropagation();
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
    const heartColors = ['#ff0000', '#ff3366', '#ff6699', '#ff99cc', '#ff66b2'];
    const heartSizes = [15, 18, 20, 23, 25, 30, 33, 35, 38, 40, 44, 47];
    const heartCount = 150;

    function createHeart() {
        const heart = document.createElement('div');
        heart.innerHTML = '❤';
        heart.className = 'falling-heart';

        const randomX = Math.floor(Math.random() * 100);
        const randomSize = heartSizes[Math.floor(Math.random() * heartSizes.length)];
        const randomColor = heartColors[Math.floor(Math.random() * heartColors.length)];
        const randomDuration = Math.random() * 3 + 3;
        const randomDelay = Math.random() * 5;

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

    for (let i = 0; i < heartCount; i++) {
        createHeart();
    }

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

document.addEventListener('DOMContentLoaded', function() {
    const thingsButton = document.getElementById('things-button');
    const thingsPopup = document.getElementById('things-popup');
    const closeButton = document.getElementById('close-things');

    thingsButton.addEventListener('click', function() {
        thingsPopup.style.display = 'flex';
    });

    closeButton.addEventListener('click', function() {
        thingsPopup.style.display = 'none';
    });

    thingsPopup.addEventListener('click', function(event) {
        if (event.target === thingsPopup) {
            thingsPopup.style.display = 'none';
        }
    });
});

// Add this to your existing JavaScript file

// Add this to your existing JavaScript file or replace the previous wheel event handler

document.addEventListener('DOMContentLoaded', function() {
    // Get reference to the things popup container and the card
    const thingsPopup = document.getElementById('things-popup');
    const thingsCard = document.querySelector('.things-card');
    
    // More robust approach to prevent scroll propagation
    thingsPopup.addEventListener('wheel', function(event) {
      // Only prevent default if the popup is visible
      if (this.style.display === 'flex') {
        event.stopPropagation();
        
        const targetElement = thingsCard;
        const scrollTop = targetElement.scrollTop;
        const scrollHeight = targetElement.scrollHeight;
        const clientHeight = targetElement.clientHeight;
        
        // Check if scrolling down and we're at the bottom
        if (event.deltaY > 0 && Math.abs(scrollHeight - clientHeight - scrollTop) < 1) {
          event.preventDefault();
        }
        
        // Check if scrolling up and we're at the top
        if (event.deltaY < 0 && scrollTop === 0) {
          event.preventDefault();
        }
      }
    }, { passive: false });
    
    // For touch devices
    thingsPopup.addEventListener('touchmove', function(event) {
      if (this.style.display === 'flex') {
        event.stopPropagation();
      }
    }, { passive: false });
  });