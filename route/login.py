from flask import Blueprint, redirect, render_template, request

from backend.user import User

login_route = Blueprint("login_route", __name__)


@login_route.route("/error/", methods=["GET"])
def error():
    msg = request.values["msg"]
    return render_template("error.html", msg=msg)


@login_route.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@login_route.route("/login/", methods=["GET"])
def login():
    username = request.values["username"]
    pwd = request.values["pwd"]
    response = User.login(username, pwd)

    if response == 1:
        return redirect("/")
    elif response == 0:
        return redirect("/error?msg=Wrong+password")
    else:
        return redirect("/error?msg=This+account+is+not+register")
