#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint

authbp = Blueprint('authbp', __name__,
        template_folder='templates')

import auth.models
@authbp.route('/')
def show():
    return 'Hello Blueprint'
