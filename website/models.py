from . import db
from sqlalchemy.sql import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    date_created = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False
    )

    listings = db.relationship(
        "Listing", backref="user", passive_deletes=True, lazy=True
    )
    reviews = db.relationship("Review", backref="user", passive_deletes=True, lazy=True)
    cart = db.relationship("Cart", backref="user", passive_deletes=True, lazy=True)
    likes = db.relationship(
        "ReviewLike", backref="user", passive_deletes=True, lazy=True
    )


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    date_created = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False
    )

    reviews = db.relationship(
        "Review", backref="listing", passive_deletes=True, lazy=True
    )
    cart = db.relationship("Cart", backref="listing", passive_deletes=True, lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    counter = db.Column(db.Integer)
    price = db.Column(db.Integer)

    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id"), nullable=False)
    likes = db.relationship(
        "ReviewLike", backref="review", passive_deletes=True, lazy=True
    )


class ReviewLike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False
    )

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    review_id = db.Column(db.Integer, db.ForeignKey("review.id"), nullable=False)
