// hides the navbar
const Hide = (CONF) => {
    if (CONF.navState === false) {return}; // check if the menu is already open
    arrangeBg(CONF);
    arrangeElements(CONF);
    CONF.navState = false;
}
// arranges the background
const arrangeBg = (CONF) => {
    const bodyPos = CONF.body.getBoundingClientRect();
    CONF.body.classList.remove("position-fixed");
    CONF.navbar.style.top = 0; // shift the navbar on the top of screen
    CONF.navbar.classList.remove("position-relative");
    document.documentElement.scrollTo({
        top: -bodyPos.top,
        left: 0,
        behavior: 'instant'
    }); // shift the document where the user view was before
}
// arranges the other elements
const arrangeElements = (CONF) => {
    CONF.scrollCover.style.opacity = "0";
    CONF.navButton.classList.remove("disabled");
    CONF.navButton.style.opacity = "100%";
    CONF.navMenu.style.left = "-85%"; // hide the mobile navbar menu
    setTimeout(() => {
        CONF.scrollCover.style.display = "none"; // don't display anymore the scroll cover after its opacity reached 0
    }, 500)
}

export default Hide;