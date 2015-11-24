#!/usr/bin/env python
# encoding: utf-8

from flask_wtf.file import FileField
from flask.ext.wtf import Form

class UpfileForm(Form):
    file = FileField('upload file')
