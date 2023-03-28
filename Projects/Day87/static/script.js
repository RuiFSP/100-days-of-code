/* Open and close navbar bar for mobile */

const mobileMenu = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

mobileMenu.addEventListener('click', () => {
    mobileMenu.classList.contains('bi-list')
        ? mobileMenu.classList.replace('bi-list', 'bi-x')
        : mobileMenu.classList.replace('bi-x', 'bi-list');
    body.classList.toggle('menu-nav-active');
});
