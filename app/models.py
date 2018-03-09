import sys
from datetime import datetime
from flask import Flask,session,abort,g
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.exc import SQLAlchemyError
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash



db = SQLAlchemy()

class User(db.Model, UserMixin):
	__tablename__ = 'users'
	id = db.Column('id',db.Integer , primary_key=True, unique = True)
	name = db.Column('first_name', db.String(60), unique=False, index=True)
	email = db.Column('email',db.String(50),unique=True , index=True)
	password = db.Column('password', db.Text)
	registered_on = db.Column('registered_on' , db.DateTime)



	def __init__(self , name=None, email=None, password=None):
		self.name = name
		self.email = email
		self.password = password
		self.registered_on = datetime.utcnow()

	def is_authenticated(self):
		return True
	

	def is_activated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False
	
	
	def get_id(self):
		try: 
			return unicode(self.id)
		except NameError:
			return str(self.id)

	
	def __repr__(self):
		return '<User %r>' % (self.email)

class Project(db.Model):
	__tablename__='projects'
	id = db.Column('id', db.Integer ,primary_key = True, unique = True)
	created_on = db.Column('date', db.DateTime)
	project_name = db.Column('project_name', db.Text(), unique = False, index = True)
	description = db.Column('description', db.String(200), unique = False, index = True)
	user_access = db.relationship('UserAccess', backref=db.backref('Project', lazy="joined"), lazy="dynamic")


	def __init__(self, project_name, description):
		self.created_on = datetime.utcnow()
		self.project_name = project_name
		self.description = description


	def get_id(self):
		return str(self.id)

	def __repr__(self):
		return '<User %r>' % (self.project_name)

class UserAccess(db.Model):
	__tablename__ = 'user_access'
	id = db.Column('id', db.Integer, primary_key = True, unique = True)
	user_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'))
	project_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))
	can_edit = db.Column('user_can_edit', db.Boolean)

	def __init__(self, user_id, project_id, can_edit):
		self.user_id = user_id
		self.project_id = project_id
		self.can_edit = can_edit

class File(db.Model):
	__tablename__="user_file"
	id = db.Column('id', db.Integer, primary_key = True, unique = True)
	uploaded_file = db.Column('uploaded_file', db.String(200), unique = False, index = True)
	file_access = db.relationship('FileAccess', backref=db.backref('File', lazy="joined"), lazy="dynamic")


	def __init__(self, uploaded_file):
		self.uploaded_file = uploaded_file


	def get_id(self):
		return str(self.id)


class FileAccess(db.Model):
	__tablename__ = "file_access"
	fa_id = db.Column('fa_id', db.Integer, primary_key = True)
	file_id = db.Column('file_id', db.Integer, db.ForeignKey('user_file.id'))
	p_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))


	def __init__(self, file_id, p_id):
		self.file_id = file_id
		self.p_id = p_id

class CirclePacking(db.Model):
	__tablename__ = "cpack"
	cp_id = db.Column('cp_id', db.Integer, primary_key = True)
	title = db.Column('title', db.String(200), unique = False)
	neutral_color = db.Column('neutral_color', db.String(15))
	root_color = db.Column('root_color', db.String(15))
	groupa_color = db.Column('groupa_color', db.String(15))
	groupb_color = db.Column('groupb_color', db.String(15))
	p_id = db.Column('project_id', db.Integer, db.ForeignKey('projects.id'))

	def __init__(self, title, neutral_color, root_color, groupa_color, groupb_color, p_id):
		self.title = title
		self.neutral_color = neutral_color
		self.root_color = root_color
		self.groupa_color = groupa_color
		self.groupb_color = groupb_color
		self.p_id = p.p_id	
