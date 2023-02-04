const urlRegEx = /'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?'/;

const Validate = (url) => {
    return urlRegEx.test(url);
};

export default Validate;