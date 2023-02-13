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

@app.route('/<refer>')
def redirect(refer):
    if refer not in ["", "about/"]:
        return render_template('redirect.html')


@app.route("/api/url/add", methods=["POST"])
@limiter.limit("5/30second")
def create():
    # print(request.get_json())
    addToDb = db.addUrl(request.get_json()["url"])

    if addToDb == 0:
        return {"status": 0x0}

    elif addToDb == 2:
        return {"status": 0x2}

    else:
        return {"status": addToDb}


@app.route("/api/url/get", methods=["POST"])
@limiter.limit("10/30second")
def get():
    getToDb = db.getUrl(request.get_json()["refer"])

    if getToDb == 0:
        return {"status": 0x0}

    elif getToDb == 3:
        return {"status": 0x3}

    else:
        return {"status": getToDb}

# @app.route('/<short>')
# def urlRedirect(short):
#     url = db.getShortUrl(short)
# 
#     if url == 0:
#         return {"status": 0x0}
# 
#     elif url == 3:
#         return {"status": 0x3}
# 
#     else:
#         return redirect(url)


if __name__ == "__main__":
    app.run("0.0.0.0", 80)
