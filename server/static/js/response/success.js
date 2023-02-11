// responds to input
const Success = (CONF, status) => {
    changeColors(CONF);
    CONF.inputField.value = status;
    CONF.inputField.classList.add("text-center")
    CONF.inputButton.innerText = "copy";
}
// change the color theme (red <-> blue)
const changeColors = (CONF) => {
    CONF.root.style.setProperty("--input-border-color", "#00e9e9");
    CONF.root.style.setProperty("--input-shadow-color", "#00e9e9");
    CONF.root.style.setProperty("--invert-icons", 1);

}

export default Success