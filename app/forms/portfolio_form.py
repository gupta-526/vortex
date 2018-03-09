from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField
from wtforms import TextAreaField, BooleanField, FileField
from wtforms.validators import Required, EqualTo, Optional, Length, Email

class Projects(Form):
	project_id = HiddenField()
	name = TextField('Project Name', validators=[Required()])
	description = TextField('Project Description', validators=[Required()])


class Files(Form):
	file_id = HiddenField()
	name = TextField('File Name')
	file_ = FileField('Raw Data File', validators=[Required()])