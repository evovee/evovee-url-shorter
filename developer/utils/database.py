import secrets
from cryptography.fernet import Fernet
from pymongo import MongoClient


GENERAL_ERROR = 0x0
INVALID_URL = 0x2
INVALID_REFER = 0x3


static_key = b""


def encrypt(url):
    return Fernet(static_key).encrypt(url.encode()).decode()


def decrypt(url):
    return Fernet(static_key).decrypt(url.encode()).decode()


class Database:
    _host = MongoClient("")
    _db = _host["developer-db-Url"]
    _collection = _db["URLs"]

    def addUrl(self, url: str) -> str | int:
        """
            url: `the url that u wanna insert into db
        """

        if url.find("http") == -1:
            return INVALID_URL

        refer = secrets.token_urlsafe(10)

        try:
            self._collection.insert_one({

                "url": encrypt(url),
                "refer": refer
            })
            return refer

        except:
            return GENERAL_ERROR

    def getUrl(self, refer: str) -> str | int:
        """
            refer: The refer string used to access to real link
        """

        if len(refer) != 14:
            return INVALID_REFER

        try:
            url = self._collection.find_one({"refer": refer}, {
                "_id": 0,
                "url": 1
            })
            return decrypt(url["url"])
        except:
            return GENERAL_ERROR
