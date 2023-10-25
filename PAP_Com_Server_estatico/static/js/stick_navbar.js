document.addEventListener("DOMContentLoaded", function () {
    var navbar = document.getElementById("navbar"); // Altere de .navbar para #navbar
    var stick = navbar.offsetTop;

    window.addEventListener("scroll", myFunction);

    function myFunction() {
        var windowScroll = window.pageYOffset || document.documentElement.scrollTop;

        if (windowScroll >= stick) {
            navbar.classList.add("stick");
        } else {
            navbar.classList.remove("stick");
        }
    }
});
