// checks if the inserted url is valid (to review)
const Validate = (url) => {
    try {
        return Boolean(new URL(url));
    } catch(e) {
        return false;
    }
};

export default Validate;
