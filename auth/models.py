#!/usr/bin/env python
# encoding: utf-8
from app import db
class User(db.Model):
    __bind_key__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True)
    password = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(120), unique = True)
    level = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r' % self.username

