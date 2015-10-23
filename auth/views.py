#!/usr/bin/env python
# encoding: utf-8

from flask import render_template, redirect, url_for, flash, request, g
from flask.ext.login import login_user, logout_user, login_required, current_user
from auth import authbp
from auth.forms import RegistrationForm, LoginForm
from app import db, lm, app
from .models import User
from hashlib import md5
@authbp.route('/register', methods = ['GET', 'POST'])
def register():
    if g.user.is_authenticated:
        return redirect(request.args.get('next') or url_for('.user'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,
                email = form.email.data,
                password = md5((form.password.data + form.username.data).encode('utf-8')).hexdigest())
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('.user'))
    return render_template('auth/register.html', form=form)

@lm.user_loader
def load_user(id):
    return User.query.get((id))

@authbp.route('/login', methods = ['GET', 'POST'])
def login():
    if g.user.is_authenticated:
        return redirect(request.args.get('next') or url_for('mainbp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data,
                password = md5((form.password.data + form.username.data).encode('utf-8')).hexdigest()).first()
        if user is None:
            flash('Invalid login, please try again.')
            return redirect(url_for('.login'))
        login_user(user)
        return redirect(request.args.get('next') or url_for('mainbp.index'))
    return render_template('auth/login.html',
            title = 'Sign In',
            form = form)

@authbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(request.args.get('next') or url_for('mainbp.index'))

@authbp.route('/user')
@login_required
def user():
    return g.user.username

@app.before_request
def before_request():
    g.user = current_user
