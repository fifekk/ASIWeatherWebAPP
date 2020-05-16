from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    #__tablename__ = "Users"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    #city = db.Column(db.String(1000))