#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
lm.init_app(app)
db = SQLAlchemy(app)
from auth import authbp
from mainapp import mainbp
from amblog import ambp

app.register_blueprint(mainbp)
app.register_blueprint(authbp, url_prefix='/auth')
app.register_blueprint(ambp, url_prefix='/amblog')

lm.login_view = 'auth.login'
