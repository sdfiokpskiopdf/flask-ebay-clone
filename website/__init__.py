from website.authfuncs import logged_in
from flask import Flask
from flask import url_for
from flask import session
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "mysecretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)

    from .buyer import buyer
    from .auth import auth

    app.register_blueprint(buyer, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    from .models import User
    from .models import Listing

    create_database(app)

    # Make permanent session
    # Set up cookies
    @app.before_request
    def setup():
        session.permanent = True

        try:
            session["logged_in"]
        except KeyError:
            session["logged_in"] = False
    
    # Inject login cookie into all/base template
    @app.context_processor
    def inject_logged_in():
        return dict(logged_in=session["logged_in"])
    
    # Solves problems related to cache
    @app.context_processor
    def override_url_for():
        return dict(url_for=dated_url_for)

    def dated_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            if filename:
                file_path = os.path.join(app.root_path,
                                    endpoint, filename)
                values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)

    return app


def create_database(app):
    if not os.path.exists("website/" + DB_NAME):
        db.create_all(app=app)
