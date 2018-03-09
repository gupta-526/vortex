from flask_wtf import Form
from wtforms import TextField, PasswordField, validators, HiddenField, TextAreaField
from wtforms import  FileField, SubmitField, ValidationError
from wtforms.validators import *

class ProjectForm(Form):
	project_id = HiddenField()
	name = TextField('Project Name', validators=[InputRequired()])
	description = TextAreaField('Project Description', validators=[InputRequired()])


class FileForm(Form):
	file_id = HiddenField()
	# name = TextField('File Name', validators=[InputRequired()])
	file_uploaded = FileField('Raw Data File', validators=[InputRequired()])
	# submit = SubmitField('Submit')

	def validate_file_upload(self,field):
		if field.data.filename[-4:].lower() != '.txt':
			raise ValidationError('Invalid file extension. Please upload a .txt file')
