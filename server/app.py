from core import *
from flask import Flask, request, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://"
)

@app.route('/')
def docs():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template('about.html')


@app.route("/api/url/add", methods=["POST"])
@limiter.limit("5/30second")
def create():
    addToDb = db.addUrl(request.get_json()["url"])

    if addToDb == 0:
        return {"status": "general error - 0x0"}
        
    elif addToDb == 2:
        return {"status": "invalid url - 0x2"}
    
    else:
        return {"status": addToDb}

@app.route("/api/url/get", methods=["POST"])
@limiter.limit("10/30second")
def get():
    addToDb = db.getUrl(request.get_json()["refer"])

    if addToDb == 0:
        return {"status": "general error - 0x0"}
        
    elif addToDb == 3:
        return {"status": "invalid refer - 0x2"}
    
    else:
        return {"status": addToDb}

if __name__ == "__main__":
    app.run("0.0.0.0", 80)
