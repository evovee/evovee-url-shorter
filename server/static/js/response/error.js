const Error = (CONF) => {
    CONF.root.style.setProperty("--input-width", "100%");
    CONF.inputField.classList.add("invalid");
    setTimeout(() => {
        CONF.inputField.classList.remove("invalid");
    }, 600)
}

export default Error;