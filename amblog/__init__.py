#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint

ambp = Blueprint('ambp', __name__,
        template_folder = 'templates',
        static_folder = 'static')
from amblog import views, models
