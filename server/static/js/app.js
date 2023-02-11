import Success from "./response/success.js";
import Error from "./response/error.js";

const App = (CONF) => {

    if (CONF.inputButton.innerText === "SHORT") {
        Add(CONF);
    } else if (CONF.inputButton.innerText === "COPY") {
        Get(CONF);
        navigator.clipboard.writeText(CONF.inputField.value);
    }
}

const Add = (CONF) => {
    fetch('/api/url/add', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "url" : CONF.inputField.value }) // esempio
    })
    .then(response => response.json())
    .then(response => {
        console.log(JSON.stringify(response));
        AddResponse(CONF, response["status"]);
    })
}
const AddResponse = (CONF, status) => {
    if ([0, 2, 3].includes(status)) {
        Error(CONF);
    } else {
        Success(CONF, status);
    }
}

const Get = (CONF) => {
    fetch('/api/url/get', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "refer" : CONF.inputField.value }) // esempio
    })
    .then(response => response.json())
    .then(response => {
        console.log(JSON.stringify(response));
        GetResponse(CONF, response["status"]);
    })
}
const GetResponse = (CONF, status) => {
    if ([0, 2, 3].includes(status)) {
        console.log("error");
    } else {
        // window.open(status);
    }
}
export default App;