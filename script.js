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

const messages = [
  "Felices 4 meses amor de mi vida. Han sido de los mejores meses de mi vida; poder amar, reime, volver a ser ese niño interior sin temor a qué diras, encontrar mi mejor amiga. Le doy las gracias a Dios cada día por tu vida, mi cielo, y por ponerte en la mía. Cada día creamos mil memorias, recuerdos y experiencias. Me encanta y no me canso de decirlo, que tengamos a Dios como el centro de esta relación, porque es la única forma que va a florecer y poder ser una pareja con propósito y del Reino. Eres la mujer más dulce, excepcional, chistosa, bella, inteligente, humilde, servicial, carismática, valiente, la mejor amiga que cualquiera pudiera desear, todo eso mil cosas más. Me gané la lotería contigo novia mía. ",
  "Gracias por elegirme todos los días, por estar a mí lado en los días buenos y no tan buenos, y por no darte por vencida conmigo.",
  "Cada vez que nos despedimos, es como si se llevaran un pedacito de mí, pero luego recuerdo la frase de Winnie de Pooh: 'Qué afortunado soy de tener algo que hace que decir adiós sea tan difícil'. Cuento los segundos de cada día para volver a verte y abrazarte con locura. ",
  "Ya 4 meses… ¿Y si hacemos que sean millones más? Felices 4 meses junto a la mejor novia del universo, que digo del universo, de todo lo que ha sido creado."
];

const messageBox = document.getElementById('message-box');
const messagePopup = document.getElementById('message-popup');
const messageItems = document.getElementById('message-items');
const cardPopup = document.getElementById('card-popup');
const cardText = document.getElementById('card-text');

messageBox.addEventListener('click', () => {
  const password = prompt("Ingresa la contraseña:");
  if (password === "15032025") {
    showMessages();
  } else {
    alert("Contraseña incorrecta 💔");
  }
});

function showMessages() {
  const envelope = document.getElementById('envelope-animation');
  envelope.style.display = 'flex';

  setTimeout(() => {
    envelope.style.display = 'none';
    messageItems.innerHTML = '';
    messages.forEach((msg, index) => {
      const li = document.createElement('li');
      li.textContent = `Mensaje ${index + 1}`;
      li.onclick = () => showCard(msg);
      messageItems.appendChild(li);
    });
    messagePopup.style.display = 'flex';
  }, 2500); // Tiempo para ver la animación
}


function closeMessagePopup() {
  messagePopup.style.display = 'none';
}

function showCard(text) {
  cardText.textContent = '';
  cardPopup.style.display = 'flex';

  let i = 0;
  function typeWriter() {
    if (i < text.length) {
      cardText.textContent += text.charAt(i);
      i++;
      setTimeout(typeWriter, 30); // Velocidad de escritura
    }
  }

  typeWriter();
}


function closeCardPopup() {
  cardPopup.style.display = 'none';
}
