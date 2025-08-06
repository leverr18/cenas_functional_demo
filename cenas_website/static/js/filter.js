document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".accordion-btn");
  const NAV_OFFSET = 100; // adjust based on your nav bar height

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetId = btn.dataset.target;
      const panel = document.getElementById(targetId);
      const isOpen = panel.classList.contains("open");

      // Collapse all others
      document.querySelectorAll(".accordion-panel").forEach(p => {
        if (p !== panel) {
          p.classList.remove("open");
          p.style.maxHeight = null;
        }
      });

      // Toggle current panel
      if (isOpen) {
        panel.classList.remove("open");
        panel.style.maxHeight = null;
      } else {
        panel.classList.add("open");
        panel.style.maxHeight = panel.scrollHeight + "px";

        // Scroll with offset
        setTimeout(() => {
          const offsetTop = panel.getBoundingClientRect().top + window.scrollY - NAV_OFFSET;
          window.scrollTo({
            top: offsetTop,
            behavior: "smooth"
          });
        }, 150);
      }
    });
  });
});









