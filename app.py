#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
app = Flask(__name__)
app.config.from_object('config')

lm = LoginManager()
db = SQLAlchemy(app)
from auth import authbp
from mainapp import mainbp
from amblog import ambp
from markwords import mwbp

app.register_blueprint(mainbp)
app.register_blueprint(authbp, url_prefix='/auth')
app.register_blueprint(ambp, url_prefix='/amblog')
app.register_blueprint(mwbp, url_prefix='/markwords')

lm.login_view = 'authbp.login'
lm.init_app(app)
