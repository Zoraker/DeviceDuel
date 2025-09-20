// const activePage = window.location.pathname;
// const navLinks = document.querySelectorAll('li a')
// console.log(navLinks)



window.addEventListener("scroll", function () {
    var nav = document.querySelector("nav");
    nav.classList.toggle("sticky", window.scrollY > 0);
})
