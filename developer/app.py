import json
from utils import Database
from flask import Flask, request


app = Flask(__name__)
db = Database()


@app.route('/')
def docs():
    return json.loads(open("./API/api.json", "r").read())


@app.route('/api/url/create', methods=["POST"])
def create():
    return {"refer": db.addUrl(request.get_json()["url"])}


@app.route('/api/url/get')
def get_url():
    args = request.args.get("refer")

    return {"url": db.getUrl(args)}


if __name__ == "__main__":
    app.run()

