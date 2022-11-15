from flask import Blueprint, redirect, render_template, request

from backend.item import Item

admin_route = Blueprint("admin_route", __name__)


@admin_route.route("/admin/", methods=["GET"])
def admin():
    items = Item.get_all_item()
    print(items)
    return render_template("admin.html")


@admin_route.route("/additem/", methods=["POST"])
def additem():
    name = request.form["name"]
    amount = request.form["amount"]
    Item.add_item(name, amount)
    return redirect("/admin")
