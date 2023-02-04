const urlRegEx = /'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?'/;

// doesn't work well -> to fix
const Validate = (url) => {
    return urlRegEx.test(url);
};

export default Validate;
