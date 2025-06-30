document.addEventListener('DOMContentLoaded', () => {
  const track = document.querySelector('.carousel-track');
  const slides = Array.from(track.children);
  const prevBtn = document.querySelector('.carousel-btn.prev');
  const nextBtn = document.querySelector('.carousel-btn.next');

  let currentIndex = 0;
  let interval;
  let slideWidth;

  // Duplicate first and last slides in JS for fake looping
  const firstClone = slides[0].cloneNode(true);
  const lastClone = slides[slides.length - 1].cloneNode(true);

  track.appendChild(firstClone);
  track.insertBefore(lastClone, slides[0]);

  const allSlides = Array.from(track.children);
  currentIndex = 1; // Start on real first slide

  function setSlidePositions() {
    slideWidth = allSlides[0].getBoundingClientRect().width;
    allSlides.forEach((slide, i) => {
      slide.style.left = `${i * slideWidth}px`;
    });
    track.style.transition = 'none';
    track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
  }

  function lazyLoad(index, callback) {
    const slide = allSlides[index];
    if (!slide) return callback();
    const img = slide.querySelector('img[data-src]');
    if (!img) return callback();

    img.src = img.dataset.src;
    img.removeAttribute('data-src');
    img.complete ? callback() : img.addEventListener('load', callback, { once: true });
  }

  function moveTo(index) {
    lazyLoad(index, () => {
      track.style.transition = 'transform 1.5s ease-in-out';
      track.style.transform = `translateX(-${index * slideWidth}px)`;
      currentIndex = index;
    });
  }

  // After transition: if we're on a clone, jump to real
  track.addEventListener('transitionend', () => {
    if (allSlides[currentIndex] === firstClone) {
      track.style.transition = 'none';
      currentIndex = 1;
      track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    } else if (allSlides[currentIndex] === lastClone) {
      track.style.transition = 'none';
      currentIndex = allSlides.length - 2;
      track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    }
  });

  function nextSlide() {
    moveTo(currentIndex + 1);
  }

  function prevSlide() {
    moveTo(currentIndex - 1);
  }

  function startCarousel() {
    interval = setInterval(() => {
      nextSlide();
    }, 5000);
  }

  function stopCarousel() {
    clearInterval(interval);
  }

  function resetCarousel() {
    stopCarousel();
    startCarousel();
  }

  document.addEventListener('visibilitychange', () => {
    document.hidden ? stopCarousel() : resetCarousel();
  });

  window.addEventListener('resize', setSlidePositions);

  nextBtn.addEventListener('click', () => {
    nextSlide();
    resetCarousel();
  });

  prevBtn.addEventListener('click', () => {
    prevSlide();
    resetCarousel();
  });

  // INIT
  setSlidePositions();
  lazyLoad(currentIndex, () => {
    track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
    startCarousel();
  });
});



