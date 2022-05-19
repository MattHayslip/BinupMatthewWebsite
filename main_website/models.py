# from email import message
# from email.policy import default
# from enum import unique

from . import DB
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime

# a ORM for db in flask
class UserContact(DB.Model, UserMixin):
    # __tablename__ = "User Contact"
    _id         = DB.Column(DB.Integer,     primary_key=True)
    full_name   = DB.Column(DB.String(150))
    email       = DB.Column(DB.String(150), unique=True)
    subject     = DB.Column(DB.String(100))
    message     = DB.Column(DB.String(250))

    def __init__(self, full_name, email, subject, message):
        self.full_name  = full_name
        self.email      = email
        self.subject    = subject
        self.message    = message