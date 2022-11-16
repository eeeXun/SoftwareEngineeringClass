from flask import Blueprint, redirect, render_template, request, session

from backend.item import Item
from backend.user import User

login_route = Blueprint("login_route", __name__)


@login_route.route("/error/", methods=["GET"])
def error():
    msg = request.values["msg"]
    return render_template("error.html", msg=msg)


@login_route.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@login_route.route("/login/", methods=["POST"])
def login():
    username = request.form["username"]
    pwd = request.form["pwd"]
    response = User.login(username, pwd)

    if response == 1:
        return redirect("/page")
    elif response == 0:
        return redirect("/error?msg=Wrong+password")
    else:
        return redirect("/error?msg=This+account+is+not+register")


@login_route.route("/page/", methods=["GET", "POST"])
def page():
    uid = session.get("id")
    username = User.get_username(uid)
    items = Item.get_all_item()
    return render_template("user.html", name=username, items=items)


@login_route.route("/register/", methods=["POST"])
def register():
    username = request.form["username"]
    pwd = request.form["pwd"]
    response = User.register(username, pwd)

    if response == 1:
        return f"""<p>{username} register success</p>
    <a href='/'><button>Back</button></a>"""
    else:
        return redirect("/error?msg=Something+wrong!")
