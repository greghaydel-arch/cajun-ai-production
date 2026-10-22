// ── Navbar scroll effect ────────────────────────────────────
const navbar = document.querySelector('.navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 40);
  });
}

// ── Hamburger / mobile nav ───────────────────────────────────
const hamburger = document.querySelector('.hamburger');
const mobileNav = document.querySelector('.mobile-nav');
if (hamburger && mobileNav) {
  const closeMenu = () => {
    hamburger.classList.remove('open');
    mobileNav.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
  };
  // A drawer opened on a phone must not cover desktop navigation after resize.
  window.matchMedia('(max-width: 900px)').addEventListener('change', closeMenu);
  document.addEventListener('click', event => {
    if (!mobileNav.contains(event.target) && !hamburger.contains(event.target)) closeMenu();
  });
  document.addEventListener('focusin', event => {
    if (!mobileNav.contains(event.target) && !hamburger.contains(event.target)) closeMenu();
  });
  hamburger.addEventListener('click', () => {
    const isOpen = hamburger.classList.toggle('open');
    mobileNav.classList.toggle('open', isOpen);
    hamburger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });
  // close on link click
  mobileNav.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      hamburger.classList.remove('open');
      mobileNav.classList.remove('open');
      hamburger.setAttribute('aria-expanded', 'false');
    });
  });
}

// ── Active nav link ──────────────────────────────────────────
const normalizedPath = path => path.replace(/\/index\.html$/, '/').replace(/\.html$/, '');
document.querySelectorAll('.nav-links a, .mobile-nav a').forEach(a => {
  if (a.hash) return;
  const target = normalizedPath(new URL(a.href).pathname);
  const currentPath = normalizedPath(window.location.pathname);
  const current = target === currentPath || (target === '/pages/blog' && currentPath.startsWith('/pages/articles/'));
  a.classList.toggle('active', current);
  if (current) a.setAttribute('aria-current', 'page');
  else a.removeAttribute('aria-current');
});

// ── Scroll fade-in (skipped if user prefers reduced motion) ──
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.opacity = '1';
        e.target.style.transform = 'translateY(0)';
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.card, .feature-card-item, .pricing-card, .yt-card, .article-card-item, .stat-item').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(24px)';
    el.style.transition = 'opacity .5s ease, transform .5s ease';
    observer.observe(el);
  });
}

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && hamburger && mobileNav && mobileNav.classList.contains('open')) {
    hamburger.classList.remove('open');
    mobileNav.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    hamburger.focus();
  }
});
