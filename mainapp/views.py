#!/usr/bin/env python
# encoding: utf-8

from flask import render_template, url_for, redirect
from app import app
from mainapp import mainbp

@mainbp.route('/')
@mainbp.route('/index')
def index():
    return render_template('mainapp/index.html')
