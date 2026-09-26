document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".menu-toggle");
  const links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", () => links.classList.toggle("open"));
  }

  document.querySelectorAll(".nav-links a").forEach(link => {
    link.addEventListener("click", () => links?.classList.remove("open"));
  });

  const hero = document.querySelector(".hero");
  const slides = [...document.querySelectorAll(".hero-slide")];
  const indicators = [...document.querySelectorAll(".hero-indicator")];

  if (hero && slides.length && slides.length === indicators.length) {
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    let currentSlide = 0;
    let rotationTimer;
    let userSelectedSlide = false;

    const showSlide = index => {
      currentSlide = index;
      slides.forEach((slide, slideIndex) => slide.classList.toggle("is-active", slideIndex === index));
      indicators.forEach((indicator, slideIndex) => {
        const isActive = slideIndex === index;
        indicator.classList.toggle("is-active", isActive);
        indicator.setAttribute("aria-pressed", String(isActive));
      });
    };

    const stopRotation = () => window.clearInterval(rotationTimer);
    const startRotation = () => {
      stopRotation();
      if (!prefersReducedMotion.matches && !userSelectedSlide) {
        rotationTimer = window.setInterval(() => showSlide((currentSlide + 1) % slides.length), 5000);
      }
    };

    indicators.forEach((indicator, index) => {
      indicator.addEventListener("click", () => {
        userSelectedSlide = true;
        showSlide(index);
        stopRotation();
      });
    });

    hero.addEventListener("mouseenter", stopRotation);
    hero.addEventListener("mouseleave", startRotation);
    hero.addEventListener("focusin", stopRotation);
    hero.addEventListener("focusout", event => {
      if (!hero.contains(event.relatedTarget)) startRotation();
    });
    startRotation();
  }
});
