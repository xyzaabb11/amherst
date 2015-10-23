#!/usr/bin/env python
# encoding: utf-8


from app import db

class Category(db.Model):
    __bind_key__ = 'amblog'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    posts = db.relationship('Posts', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name

class Posts(db.Model):
    __bind_key__ = 'amblog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    content = db.Column(db.Text)
    category_id = db.Column(db.ForeignKey('category.id'))
    author = db.Column(db.Integer)

    def __repr__(self):
        return '<Posts %r>' % self.title
