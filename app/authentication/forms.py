from flask_wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField, TextAreaField, BooleanField

from wtforms.validators import *
class SignupForm(Form):
    name = TextField('Name', validators=[InputRequired(), 
            NoneOf(values='!@#$%^&*(){}:<>?/][\=,_', message='Please enter a valid name')])
    email = TextField('Email address', validators=[
            InputRequired(message='Please provide a valid email address'),
            Length(min=6, message='Email address too short'),
            Email(message=(u'That\'s not a valid email address.'))
            ])
    password = PasswordField('Password', validators=[
            InputRequired(),
            Length(min=6, message='Please give a longer password'),
            EqualTo("check_password", message='Passwords Do Not Match')
            ])
    check_password = PasswordField('Re-enter password', validators=[InputRequired()])
    

class SigninForm(Form):
	email= TextField('Email address', validators=[InputRequired(), Email(message='Please provide a valid email address or password')])
	password = PasswordField('Password', validators = [InputRequired()])
	remember_me = BooleanField('Remember me', default = False)