from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is a home page"


@app.route("/loginpage")
def login():
    return "This is a login page"


import controller.user_controller