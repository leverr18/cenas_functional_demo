document.addEventListener('DOMContentLoaded', () => {
  const map = L.map('map').setView([29.99, -95.48], 10.5);  // Houston/Tomball/Woodlands view

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
  }).addTo(map);

  // Use Flask-rendered DOM list instead of fetching again
  const listItems = document.querySelectorAll('#location-list li');

  listItems.forEach(li => {
    const lat = parseFloat(li.dataset.lat);
    const lng = parseFloat(li.dataset.lng);
    const name = li.querySelector('strong')?.textContent || 'Location';
    const address = li.innerHTML;

    const marker = L.marker([lat, lng])
      .addTo(map)
      .bindPopup(address);

    li.addEventListener('click', () => {
      map.setView([lat, lng], 14);
      marker.openPopup();
    });
  });
});

