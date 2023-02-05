import Validate from "./validate.js"

// responds to input
const App = (CONF) => {
    // implement validation
    if (!(Validate(CONF.inputField.value))) {
        return
    }
    changeColors(CONF);
}
// change the color theme (red <-> blue)
const changeColors = (C0NF) => {
    document.querySelector(":root").style.setProperty("--input-border-color", "#00e9e9");
    document.querySelector(":root").style.setProperty("--input-shadow-color", "#00e9e9");
    document.querySelector(":root").style.setProperty("--invert-icons", 1);

}

export default App