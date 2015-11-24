#!/usr/bin/env python
# encoding: utf-8

from flask import render_template
from markwords import mwbp
from markwords.forms import UpfileForm
from werkzeug import secure_filename

@mwbp.route('/index')
@mwbp.route('/')
def index():
    form = UpfileForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/'+ filename)
    else:
        filename = None
    return render_template('markwords/index.html', form = form, filename = filename)


