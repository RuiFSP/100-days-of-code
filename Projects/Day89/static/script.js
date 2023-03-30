// Open and close navbar bar for mobile

const mobileMenu = document.querySelector('.menu-mobile');
const body = document.querySelector('body');

mobileMenu.addEventListener('click', () => {
    mobileMenu.classList.contains('bi-list')
        ? mobileMenu.classList.replace('bi-list', 'bi-x')
        : mobileMenu.classList.replace('bi-x', 'bi-list');
    body.classList.toggle('menu-nav-active');
});

// Close menu when an item is clicked and change icon to list

const navItem = document.querySelectorAll('.nav-item')

navItem.forEach(item => {
    item.addEventListener("click", () => {
        if (body.classList.contains("menu-nav-active")) {
            body.classList.remove("menu-nav-active")
            mobileMenu.classList.replace('bi-x', 'bi-list')
        }
    })
})

// animate all data-anime items

const item = document.querySelectorAll("[data-anime]");

const animeScroll = () => {
    const windowTop = window.pageYOffset + window.innerHeight * 0.85;

    item.forEach(el => {
        if (windowTop > el.offsetTop) {
            el.classList.add("animate")
        } else {
            el.classList.remove("animate")
        }
    });
};

window.addEventListener("scroll", () => {
    animeScroll();
})

// send loading button

const btnSend = document.querySelector("btn-send")
const btnSendLoader = document.querySelector("btn-send-loader")


btnSend.addEventListener("click", () => {
    btnSendLoader.style.display = "block";
    btnSend.style.display = "none";
})

//delete confirmation message after 5 seg

setTimeout(() => {
    document.querySelector('msg-alert').style.display = 'none';
}, 3000)
