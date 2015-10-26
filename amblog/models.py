#!/usr/bin/env python
# encoding: utf-8

import datetime
from app import db
'''
class Category(db.Model):
    __bind_key__ = 'amblog'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)

    posts = db.relationship('Posts', backref='category', lazy='dynamic')

    def __repr__(self):
        return '<Category %r>' % self.name
'''
class Posts(db.Model):
    __bind_key__ = 'amblog'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    content = db.Column(db.Text)
    #category_id = db.Column(db.ForeignKey('category.id'))
    author = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, default = datetime.datetime.utcnow)
    update_time = db.Column(db.DateTime)
    publish = db.Column(db.Boolean, default = False)
    publish_time = db.Column(db.DateTime)

    tag_list = db.relationship('Tag', secondary=lambda: PostAndTag.__table__)

    def __repr__(self):
        return '<Posts %r>' % self.title

class Tag(db.Model):
    __bind_key__ = 'amblog'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), server_default='')
    author = db.Column(db.Integer)

    def __repr__(self):
        return '<Tag %r>' % self.name

class PostAndTag(db.Model):
    __bind_key__ = 'amblog'
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.Integer, db.ForeignKey('posts.id'), index = True)
    tag = db.Column(db.Integer, db.ForeignKey('tag.id'), index = True)

