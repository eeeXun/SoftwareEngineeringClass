from flask import Blueprint, render_template

admin_route = Blueprint("admin_route", __name__)


@admin_route.route("/admin/", methods=["GET"])
def admin():
    return render_template("admin.html")
