
const buttonLink = document.querySelector(".button-link");
const navbarMenu = document.querySelector(".menuNavbar");
var navbarState = false;

buttonLink.addEventListener("click",()=>{

    if (navbarState == false) {
        navbarMenu.style.left = "0";
        navbarState = true;
    } else if (navbarState == true){
        navbarMenu.style.left = "-100rem";
        navbarState = false;
    }
})