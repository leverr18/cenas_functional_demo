document.addEventListener('DOMContentLoaded', () => {
  const buttons = document.querySelectorAll('.filter-btn');
  const menuCards = document.querySelectorAll('.menu-card');
  const specialsBanner = document.querySelector('.specials-banner');
  const menuGrid = document.querySelector('.menu-grid');

  let isInitialLoad = true;

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const filter = btn.dataset.filter;

      // Toggle active button
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      if (filter === 'specials') {
        specialsBanner.style.display = 'block';
        menuGrid.style.display = 'none';
      } else {
        specialsBanner.style.display = 'none';
        menuGrid.style.display = 'grid';

        // Show only matching cards
        menuCards.forEach(card => {
          const category = card.dataset.category;
          card.style.display = (filter === category) ? 'block' : 'none';
        });
      }

      // ✅ Scroll to menu grid on mobile — but skip on initial load
      if (!isInitialLoad && window.innerWidth <= 768) {
        if (menuGrid) {
          menuGrid.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }

      isInitialLoad = false; // mark that we’re past initial load
    });
  });

  // Trigger click on the first real category tab (skip specials) on page load
  if (buttons[1]) {
    buttons[1].click();
  }

  // Optional: category toggle logic (if you have any collapsible categories)
  const toggles = document.querySelectorAll('.category-toggle');
  toggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
      const items = toggle.nextElementSibling;
      items.style.display = (items.style.display === 'block') ? 'none' : 'block';
    });
  });
});




