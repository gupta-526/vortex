from flask_wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField, TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Optional, Length, Email

class SignupForm(Form):
    name = TextField('Name', validators=[Required()])
    email = TextField('Email address', validators=[
            Required('Please provide a valid email address'),
            Length(min=6, message=(u'Email address too short')),
            Email(message=(u'That\'s not a valid email address.'))
            ])
    password = PasswordField('Password', validators=[
            Required(),
            Length(min=6, message=(u'Please give a longer password'))
            ])
    # check_password = PasswordField('Re-enter password', validators[Required()])
    

class SigninForm(Form):
	email= TextField('Email address', validators=[Required()])
	password = PasswordField('Password', validators = [Required()])
	remember_me = BooleanField('Remember me', default = False)