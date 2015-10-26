#!/usr/bin/env python
# encoding: utf-8

import datetime
from flask import render_template, flash, request,g
from flask.ext.login import login_required
from amblog import ambp
from app import db
from amblog.models import *
import json

@ambp.route('/index')
@ambp.route('/')
def index():
    posts = Posts.query.all()
    return render_template('index.html', posts = posts)

@ambp.route('/write', methods=('POST', 'GET'))
@login_required
def write():
    if request.method == 'POST':
        print(request.form)
    return render_template('amblog/write.html')

@ambp.route('/savepost', methods=('POST', 'GET'))
@login_required
def savepost():
    if request.method == 'POST':
        print(type(request.form['title']))
        post = Posts.query.get(1)
        print(post)
        if post is None:
            post = Post()
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = g.user.id
        post.update_time = datetime.datetime.utcnow()
        post.tag_list = []
        print(post)
        db.session.add(post)
        db.session.commit()
        return json.dumps({'status': 'OK'},)

@ambp.route('/show/<username>')
def showpost(username):
    pass
