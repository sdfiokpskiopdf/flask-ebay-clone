from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import session

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    pass  # If GET display login page, otherwise redirect to home page.


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    pass  # If GET display sign up page, otherwise redirect to home page(logged in).


@auth.route("/logout")
def logout():
    pass  # Remove the logged in session and redirect to the home page(logged out).
