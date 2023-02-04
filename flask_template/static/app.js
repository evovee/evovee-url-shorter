import Validate from "./validate.js"

const App = (CONF) => {
    if (!Validate(CONF.inputField.value)) {
        // error message
        console.log('error');
    }


}

export default App