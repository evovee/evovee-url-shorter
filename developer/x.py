import secrets


while True:
    print(len(secrets.token_urlsafe(10)))