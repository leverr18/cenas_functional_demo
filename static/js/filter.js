document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;

    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const filter = btn.dataset.filter;

    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    document.querySelectorAll('.menu-card').forEach(card => {
      const category = card.dataset.category;
      if (filter === 'specials') {
        document.querySelector('.specials-banner').style.display = 'block';
        card.style.display = 'none';
      } else {
        document.querySelector('.specials-banner').style.display = 'none';
        card.style.display = (filter === category) ? 'block' : 'none';
      }
    });

    // ✅ New: scroll to menu-grid on mobile
    if (window.innerWidth <= 768) {
      const grid = document.querySelector('.menu-grid');
      if (grid) {
        grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }
  });
});
    if (filter === 'specials') {
      specialsBanner.style.display = 'block';
      menuGrid.style.display = 'none';
    } else {
      specialsBanner.style.display = 'none';
      menuGrid.style.display = 'grid';

      document.querySelectorAll('.menu-card').forEach(card => {
        const category = card.dataset.category;
        if (filter === category) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    }
  });
});

// trigger click on the first category tab on page load (skip specials)
document.querySelectorAll('.filter-btn')[1].click();

document.addEventListener('DOMContentLoaded', () => {
  const toggles = document.querySelectorAll('.category-toggle');

  toggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
      const items = toggle.nextElementSibling;
      items.style.display = (items.style.display === 'block') ? 'none' : 'block';
    });
  });
});


