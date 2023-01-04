from flask import Flask, render_template, request, session
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "ABC"
socketio = SocketIO(app)
global answer


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
    global answer
    answer = data[1]
    socketio.emit("set_qa", data)


@socketio.on("send_message")
def send_message(data):
    global answer
    username = session.get("username")
    socketio.emit("set_box", f"{username}: {data}<br>")

    if data == answer:
        socketio.emit("set_box", f"{username} get the answer!<br>")


if __name__ == "__main__":
    app.debug = True
    socketio.run(app, host="0.0.0.0")
