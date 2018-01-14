"""User

Model representing a user in the system
"""
from config.db import db

class User(db.Model):
    __tablename__ = 'users'

    # model schema
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, email, username, password):
        self._id = _id
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def find(cls, id):
        return cls.query.filter_by(id=id)

    @classmethod
    def find_by(cls, **kwargs):
        return cls.query.filter_by(kwargs).first()

    @classmethod
    def first(cls):
        return cls.query(cls).one()

    @classmethod
    def all(cls):
        return cls.query(cls)

    @classmethod
    def new(cls):
        pass

    @classmethod
    def create(cls, **kwargs):
        db.session.add(kwargs)
        db.session.commit()

    def update(self):
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()
