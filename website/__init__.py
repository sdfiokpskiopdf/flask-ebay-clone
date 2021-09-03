from flask import Flask
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

    return app


def create_database(app):
    if not os.path.exists("website/" + DB_NAME):
        db.create_all(app=app)
