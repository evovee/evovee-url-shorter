// shows the navbar
const Show = (CONF) => {
    CONF.scrollCover.style.display = "block"; // display the scroll cover before the function is executed
    setTimeout(() => {
        fixBg(CONF);
        arrangeElements(CONF)
    }, 1)
}
// prevents the scroll
const fixBg = (CONF) => {
    const bodyPos = CONF.body.getBoundingClientRect();
    CONF.body.classList.add("position-fixed");
    CONF.body.style.top = `${bodyPos.top}px`; // shift the body where the user view is
    CONF.navbar.classList.add("position-relative");
    CONF.navbar.style.top = `${-bodyPos.top}px`; //shift the navbar on the top of the screen
    CONF.navMenu.style.top = 0; //shift the mobile navbar menu on the top of the screen
}
// arranges the other elements
const arrangeElements = (CONF) => {
    CONF.scrollCover.style.opacity = "80%";
    CONF.navButton.classList.add("disabled");
    CONF.navButton.style.opacity = "0";
    CONF.navMenu.style.left = "0"; // show the mobile navbar menu
    CONF.navState = true;
}

export default Show;