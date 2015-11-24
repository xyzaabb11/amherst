#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint

mwbp = Blueprint('mwbp', __name__,
        template_folder = 'templates',
        static_folder = 'static')

from markwords import views
