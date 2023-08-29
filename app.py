from flask import Flask

app = Flask(__name__)


@app.route("/", method=["GET"])
def code():
    pass