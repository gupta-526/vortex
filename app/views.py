import os,sys,string,random,smtplib
from flask import Flask,session,render_template,request,abort,g, Blueprint
from flask import redirect,current_app,url_for,flash,send_from_directory
from werkzeug import SharedDataMiddleware,secure_filename
from flask_sqlalchemy import SQLAlchemy
# from app.circle_packing import process_fc_data,mtable_to_json
from datetime import datetime
from flask_login import LoginManager
from flask_login import UserMixin as user_mixin
from flask_login import login_user , logout_user , current_user , login_required
from app.models import db, User, Project, UserAccess
from flask_bcrypt import generate_password_hash, check_password_hash
# from app.authentication.forms import *

# app=create_app('../config')

views=Blueprint('views',__name__,template_folder='templates',static_folder='static')

@views.route("/")
def index():

	return render_template("index.html")

	
@views.route('/<path:resource>')
def serveStaticResource(resource):
	return send_from_directory('app/static/', resource)
	

# #method to generate a unique name for the new converted .json file
def random_sufix(length=6, chars=string.ascii_uppercase+string.digits):
	return ''.join([random.choice(chars) for _ in range(length)])
	
# #method to render template using various variables from form and the filename+path


