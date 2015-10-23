#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint

mainbp = Blueprint('mainbp', __name__,
        template_folder = 'templates')
from mainapp import views
#app = Flask(__name__)
#app.register_blueprint(authbp, url_prefix='/auth')
def index():
    return 'Hello Amherst'
