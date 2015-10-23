#!/usr/bin/env python
# encoding: utf-8
from app import db
class User(db.Model):
    __bind_key__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(120), unique = True)
    level = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<User %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
