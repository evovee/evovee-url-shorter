import App from "./app.js";

const ShortUrl = (CONF) => {
    let url = document.querySelector("#io-field").value;
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/api/url/create", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            App(CONF);
            CONF.inputField.value = xhr.responseText;
        }
    };
    xhr.send(JSON.stringify({ url: url }));
}

export default ShortUrl;