import Validate from "./validate.js"

// responds to input
const App = (CONF) => {
    // implement validation
    if (!(Validate(CONF.inputField.value))) {
        return
    }
    changeColors(CONF);
    CONF.inputField.value = "";
    CONF.inputField.classList.add("text-center")
    CONF.inputButton.value = "copy";
}
// change the color theme (red <-> blue)
const changeColors = (CONF) => {
    CONF.root.style.setProperty("--input-border-color", "#00e9e9");
    CONF.root.style.setProperty("--input-shadow-color", "#00e9e9");
    CONF.root.style.setProperty("--invert-icons", 1);

}

export default App