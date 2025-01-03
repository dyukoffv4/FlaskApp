from . import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    win_plays = db.Column(db.Integer)
    all_plays = db.Column(db.Integer)
