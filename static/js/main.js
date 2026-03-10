/* ============================================================
   CHINMAY CHAUDHARI PORTFOLIO – main.js
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  // ------------------------------------------------------------------
  // 1. INITIALISE AOS (Animate On Scroll)
  // ------------------------------------------------------------------
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 700,
      once: true,
      offset: 60,
      easing: 'ease-out-cubic',
    });
  }

  // ------------------------------------------------------------------
  // 2. NAVBAR: add 'scrolled' class for glassmorphism toggle
  // ------------------------------------------------------------------
  const navbar = document.getElementById('mainNavbar');
  if (navbar) {
    const onScroll = () => {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // run once on load
  }

  // ------------------------------------------------------------------
  // 3. SKILL BAR ANIMATION (IntersectionObserver)
  // ------------------------------------------------------------------
  const skillBars = document.querySelectorAll('.skill-bar-fill');
  if (skillBars.length > 0) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const bar = entry.target;
            const targetWidth = bar.getAttribute('data-width') || '0';
            // slight delay per card for stagger effect
            setTimeout(() => {
              bar.style.width = targetWidth + '%';
            }, 150);
            observer.unobserve(bar);
          }
        });
      },
      { threshold: 0.2 }
    );
    skillBars.forEach((bar) => observer.observe(bar));
  }

  // ------------------------------------------------------------------
  // 4. SMOOTH SCROLLING for in-page anchor links
  // ------------------------------------------------------------------
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const navbarHeight = navbar ? navbar.offsetHeight : 70;
        const top = target.getBoundingClientRect().top + window.scrollY - navbarHeight - 10;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  // ------------------------------------------------------------------
  // 5. NAVBAR: close mobile menu on nav-link click
  // ------------------------------------------------------------------
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
  const navCollapse = document.getElementById('navbarNavigation');
  if (navCollapse) {
    navLinks.forEach((link) => {
      link.addEventListener('click', () => {
        const bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
        if (bsCollapse) bsCollapse.hide();
      });
    });
  }

  // ------------------------------------------------------------------
  // 6. AUTO-DISMISS flash messages after 5 seconds
  // ------------------------------------------------------------------
  const alerts = document.querySelectorAll('.messages-container .alert');
  alerts.forEach((alert) => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      if (bsAlert) bsAlert.close();
    }, 5000);
  });

  // ------------------------------------------------------------------
  // 7. CONTACT FORM: basic client-side UX (re-enable button on error)
  // ------------------------------------------------------------------
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', function () {
      const submitBtn = document.getElementById('contactSubmitBtn');
      if (submitBtn && this.checkValidity()) {
        submitBtn.innerHTML = '<i class="bi bi-hourglass-split me-2"></i>Sending...';
        submitBtn.disabled = true;
      }
    });
  }

});
