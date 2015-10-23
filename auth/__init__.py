#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint

authbp = Blueprint('authbp', __name__,
        template_folder='templates',
        static_folder='static')

from auth import views
@authbp.route('/')
@authbp.route('/index')
def show():
    return 'Hello Blueprint'
