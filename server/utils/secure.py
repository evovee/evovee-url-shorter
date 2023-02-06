from cryptography.fernet import Fernet

static_key = b"bG4bmFDECl9_2WxFkcOAW2kErRenpqIgDtVPtnU9kmk="


def encrypt(url):
    return Fernet(static_key).encrypt(url.encode()).decode()


def decrypt(url):
    return Fernet(static_key).decrypt(url.encode()).decode()
