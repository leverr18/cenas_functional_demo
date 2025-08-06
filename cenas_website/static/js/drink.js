document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".drink-accordion-btn"); // using your consistent (misspelled but fine) class

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetId = btn.dataset.target;
      const panel = document.getElementById(targetId);

      // Collapse all other panels
      document.querySelectorAll(".accordion-panel").forEach(p => {
        if (p !== panel) {
          p.classList.remove("open");
          p.style.maxHeight = null;
        }
      });

      // Toggle the selected panel
      const isOpen = panel.classList.contains("open");
      panel.classList.toggle("open");

      if (isOpen) {
        panel.style.maxHeight = null;
      } else {
        panel.style.maxHeight = panel.scrollHeight + "px";

        // Offset scroll position to account for fixed navbar height
        const offset = 100; // Adjust to match your nav height
        const y = panel.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top: y, behavior: "smooth" });
      }
    });
  });
});
