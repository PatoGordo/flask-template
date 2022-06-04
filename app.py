from flask import Flask
from use_cases.home.controller import HomeController

app = Flask(__name__)


@app.route("/", methods=["POST"])
def home():
    return HomeController().execute()
