#!/usr/bin/env python
# encoding: utf-8

from flask import render_template, flash
from flask.ext.login import login_required
from amblog import ambp

@ambp.route('/index')
@ambp.route('/')
def index():
    return render_template('index.html')

@ambp.route('/write')
@login_required
def write():
    return render_template('amblog/write.html')


