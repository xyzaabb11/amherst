#!/usr/bin/env python
# encoding: utf-8

import datetime
from flask import render_template, flash, request,g,jsonify
from flask.ext.login import login_required
from amblog import ambp
from app import db
from amblog.models import *
import json

@ambp.route('/index')
@ambp.route('/')
def index():
    posts = Posts.query.all()
    return render_template('amblog/index.html', posts = posts)

@ambp.route('/write', methods=('POST', 'GET'))
@login_required
def write():
    post = Posts.query.filter_by(author = g.user.id, last_updated = True).first();
    id = 0
    if post is not None:
        id = post.id
    posts = {}
    for p in Posts.query.all():
        posts[str(p.id)] = p.title
    return render_template('amblog/write.html', id = id, posts=(posts))

@ambp.route('/savepost', methods=('POST', 'GET'))
@login_required
def savepost():
    if request.method == 'POST':
        print((request.form['id']))
        post = Posts.query.get(request.form['id'])
        #print(post)
        if post is None:
            post = Posts()
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = g.user.id
        post.update_time = datetime.datetime.utcnow()
        post.tag_list = []
        print(post)
        db.session.add(post)
        db.session.commit()
        print(post.create_time)
        return json.dumps({'status': 'OK','id': post.id, 'title': post.title})

@ambp.route('/show/<int:id>')
def show(id):
    post = Posts.query.get(id)
    if post is not None:
        return post.content
    return 'Post id not found!'

@ambp.route('/showpost/<int:id>')
def showpost(id):
    post = Posts.query.get(id)
    if post is not None:
        return render_template("amblog/post.html", post = post, id=id)
    return 'Post id not found!'
@ambp.route('/getpost/<int:id>/<int:oldid>')
def getpost(id, oldid):
    post = Posts.query.get(id)
    if post is not None:
        oldpost = Posts.query.get(oldid)
        if oldpost is not None:
            oldpost.last_updated = False
            db.session.add(oldpost)
            db.session.commit()
        post.last_updated = True
        db.session.add(post)
        db.session.commit()

        return post.content
    return 'Post id not found!'
