from functools import wraps
from flask import session
from flask import flash
from flask import redirect
from flask import url_for


def logged_in(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("logged_in"):
            return f(*args, **kwargs)
        else:
            flash("Please log in first.", "error")
            return redirect(url_for("auth.login"))

    return decorated_function
