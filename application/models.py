"""
DATABASE MODELS
"""


from .database import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    lname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String)

class Tracker(db.Model):
    __tablename__ = 'tracker'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String, nullable=False)
    type = db.Column(db.Integer, nullable = False)
    choices = db.Column(db.String)
    details = db.Column(db.String)
    time = db.Column(db.String, nullable=False)

class Logs(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("user.id"))
    tid = db.Column(db.Integer, db.ForeignKey("tracker.id"))
    value = db.Column(db.String, nullable = False)
    data = db.Column(db.String)
    time = db.Column(db.String, nullable=False)


