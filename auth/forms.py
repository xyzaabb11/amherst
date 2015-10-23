#!/usr/bin/env python
# encoding: utf-8

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, validators
from auth.models import User

class RegistrationForm(Form):
    username = StringField('Username', [validators.Required(), validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Required(), validators.Length(min=6, max=35), validators.Email()])
    password = PasswordField('Password', [validators.Required(),validators.EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Repeat Password')

    def validate(self):
        user = User.query.filter_by(username = self.username.data).first()
        print(user)
        if user != None:
            print(self.errors)
            self.username.errors = ('This username is already existed',)
            return False
        user = User.query.filter_by(email = self.email.data).first()
        if user != None:
            self.email.errors = ('This email address is already existed',)
            return False
        if not Form.validate(self):
            return False
        return True

class LoginForm(Form):
    username = StringField('Username', [validators.Required()])
    password = StringField('Password', [validators.Required()])

    def validate(self):
        if not Form.validate(self):
            return False
        return True
