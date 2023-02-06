import secrets
import utils.errors as errors
import utils.secure as secure
from urllib.parse import urlparse
from pymongo import MongoClient


error = errors.ErrorCodes()


def validate_url(url):
    try:
        parse = urlparse(url)
        return all([parse.scheme, parse.netloc])

    except ValueError:
        return False


class Database:
    client = MongoClient("mongodb://localhost:27017")
    db = client["developer-db-Url"]
    collection = db["URLs"]

    def addUrl(self, url: str) -> str | int:
        try:
            if validate_url(url):
                refer = secrets.token_hex(7)
                self.collection.insert_one({
                    "url": secure.encrypt(url),
                    "refer": refer
                })
                return refer
            else:
                return error.INVALID_REFER
        except:
            return error.GENERAL_ERROR

    def getUrl(self, refer: str) -> str | int:

        if len(refer) != 14:
            return error.INVALID_REFER

        try:
            url = self.collection.find_one({"refer": refer})
            return secure.decrypt(url["url"])
        except:
            return error.GENERAL_ERROR


