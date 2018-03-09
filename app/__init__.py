# package that works like the wsgi package in the bio app
import os,sys
import os.path as osp
from datetime import *
from flask import Flask, Blueprint
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.models import db

 
flask_app = Flask(__name__)
flask_app.config.from_pyfile('../config.py')

flask_bcrypt = Bcrypt(flask_app)

login_manager = LoginManager()
login_manager.init_app(flask_app)
login_manager.login_view = "login"
# with flask_app.app_context():
# db=SQLAlchemy(flask_app)
db.init_app(flask_app)
#import views
from  app.views import views
from app.authentication.views import authentication
from app.portfolio.views import portfolio
from app.cpack.views import cpack
from app.bubble_viz.views import bubble
from app.radar.views import radar
import app.forms 
flask_app.register_blueprint(views)
flask_app. register_blueprint(authentication)
flask_app.register_blueprint(portfolio)
flask_app.register_blueprint(cpack)
flask_app.register_blueprint(bubble)
flask_app.register_blueprint(radar)
