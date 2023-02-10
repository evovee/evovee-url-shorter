import App from "./app.js";

const ShortUrl = (CONF) => {
    let data = {
        url : document.querySelector("#io-field").value
    }

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/api/url/add", true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            App(CONF);
            CONF.inputField.value = xhr.responseText;
        }
    };
    xhr.send(JSON.stringify(data));
}

export default ShortUrl;