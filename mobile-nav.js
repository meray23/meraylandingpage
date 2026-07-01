
  // Mobile Drawer toggle
const hamburger = document.getElementById('hamburgerBtn');
const drawer = document.getElementById('mobileDrawer');
const overlay = document.getElementById('drawerOverlay');
const closeBtn = document.getElementById('drawerCloseBtn');

function openDrawer() {
    hamburger.classList.add('active');
    drawer.classList.add('open');
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
}

function closeDrawer() {
    hamburger.classList.remove('active');
    drawer.classList.remove('open');
    overlay.classList.remove('open');
    document.body.style.overflow = '';
}

hamburger.addEventListener('click', function(e) {
    e.stopPropagation();
    if (drawer.classList.contains('open')) {
        closeDrawer();
    } else {
        openDrawer();
    }
});

closeBtn.addEventListener('click', closeDrawer);
overlay.addEventListener('click', closeDrawer);

// Close drawer when clicking a link
document.querySelectorAll('.hdr__nav-drawer .nav-lnk').forEach(link => {
    link.addEventListener('click', closeDrawer);
});

// Close drawer on escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
        closeDrawer();
    }
});

// Close on resize to desktop
window.addEventListener('resize', () => {
    if (window.innerWidth > 768 && drawer.classList.contains('open')) {
        closeDrawer();
    }
});