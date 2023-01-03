from flask import Flask, render_template, request, session
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "ABC"
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/question")
def question():
    return render_template("question.html")


@app.route("/login")
def login():
    username = request.values["username"]
    session["username"] = username
    return render_template("login.html", username=username)


@socketio.on("set")
def set(data):
    socketio.emit("set_qa", data)


if __name__ == "__main__":
    app.debug = True
    socketio.run(app, host="0.0.0.0")
