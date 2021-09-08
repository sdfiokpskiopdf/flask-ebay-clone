from operator import methodcaller
import re
from website.authfuncs import logged_in
from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import session

buyer = Blueprint("buyer", __name__)


@buyer.route("/", methods=["GET", "POST"])
@buyer.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        query = request.form.get("query")
        return redirect(url_for("buyer.search", query=query))
    else:
        return render_template("home.html")


@buyer.route("/search/<query>")
def search(query):
    return f"{query}"


@buyer.route("/item/<id>")
def item(id):
    pass  # Return item page based on ID
