"""User

Model representing a user in the system
"""
from config.db import db

class User(db.Model):
    __tablename__ = 'users'

    # model schema
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, email, username, password):
        self._id = _id
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def find_by(cls, **kwargs):
        pass

    @classmethod
    def first(cls):
        pass

    @classmethod
    def all(cls):
        pass

    @classmethod
    def new(cls):
        pass

    @classmethod
    def create(cls):
        pass

    def update(self):
        pass

    def destroy(self):
        pass
