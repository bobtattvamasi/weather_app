# models/user.py
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(80), unique=True, nullable=False)
    searches = db.relationship('SearchHistory', backref='user', lazy=True)