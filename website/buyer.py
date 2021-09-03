from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import session

buyer = Blueprint("views", __name__)


@buyer.route("/")
@buyer.route("/home", methods=["GET", "POST"])
def home():
    pass  # If GET, display home page. If POST, redirect to /search/<query>


@buyer.route("/search/<query>")
def search(query):
    pass  # Query database for results


@buyer.route("/item/<id>")
def item(id):
    pass  # Return item page based on ID\
