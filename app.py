#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
from auth import authbp
from mainapp import mainbp


app.register_blueprint(mainbp)
app.register_blueprint(authbp, url_prefix='/auth')

