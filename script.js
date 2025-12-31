(() => {
  'use strict';

  document.addEventListener('DOMContentLoaded', async () => {
    const images = await loadManifest();
    renderGallery(images);
    setupOverlayAndCards();
  });

  async function loadManifest() {
    const res = await fetch('./gallery.json', { cache: "no-store" });
    if (!res.ok) throw new Error("Couldn't load gallery.json");
    return await res.json(); // [{id, full, thumb}, ...]
  }

  function renderGallery(items) {
    const gallery = document.getElementById('gallery');
    if (!gallery) return;

    const frag = document.createDocumentFragment();

    for (const it of items) {
      const card = document.createElement('div');
      card.className = 'card';
      card.dataset.full = it.full;

      const inner = document.createElement('div');
      inner.className = 'card-inner';

      const front = document.createElement('div');
      front.className = 'card-front';

      const img = document.createElement('img');
      img.alt = it.id;
      img.loading = 'lazy';
      img.decoding = 'async';
      img.width = 240;
      img.height = 240;
      img.src = it.thumb; // FAST thumb
      front.appendChild(img);

      const back = document.createElement('div');
      back.className = 'card-back';
      back.innerHTML = `<p><strong>${it.id}</strong></p><p>💗</p>`; // you can replace later

      inner.appendChild(front);
      inner.appendChild(back);
      card.appendChild(inner);
      frag.appendChild(card);
    }

    gallery.innerHTML = '';
    gallery.appendChild(frag);
  }

  function setupOverlayAndCards() {
    const overlay = document.createElement('div');
    overlay.className = 'overlay';
    document.body.appendChild(overlay);

    const gallery = document.getElementById('gallery');
    if (!gallery) return;

    let openCard = null;

    const close = () => {
      if (openCard) {
        openCard.classList.remove('flipped', 'enlarged');
        openCard = null;
      }
      overlay.style.display = 'none';
      document.body.classList.remove('modal-open');
    };

    const open = (card) => {
      // if same card already open, just flip
      if (openCard === card && card.classList.contains('enlarged')) {
        card.classList.toggle('flipped');
        return;
      }

      if (openCard && openCard !== card) {
        openCard.classList.remove('flipped', 'enlarged');
      }
      openCard = card;

      // swap thumb -> full only when opened
      const img = card.querySelector('img');
      const full = card.dataset.full;
      if (img && full && img.src !== full) img.src = full;

      card.classList.add('enlarged', 'flipped');
      overlay.style.display = 'block';
      document.body.classList.add('modal-open');
    };

    gallery.addEventListener('click', (event) => {
      const card = event.target.closest('.card');
      if (!card) return;
      event.stopPropagation();
      open(card);
    });

    overlay.addEventListener('click', close);
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
    document.addEventListener('click', (event) => {
      if (openCard && !event.target.closest('.card')) close();
    });
  }
})();
