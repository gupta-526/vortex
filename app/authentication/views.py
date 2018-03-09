from flask import render_template, request
from flask import redirect, url_for, session
from flask_login import LoginManager, login_user , logout_user, current_user, login_required
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash
import os,sys,string,random,smtplib
from flask import Flask,session,render_template,request, g
from app.models import db, User
from flask import Blueprint
from app.authentication.forms import *
import sys
from app import flask_bcrypt, login_manager

authentication = Blueprint('authentication', __name__, template_folder='../app/templates', static_folder='../app/static')




@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

@authentication.route("/signin", methods=['GET', 'POST'])
def signin():

	form = SigninForm(request.form)
	if form.validate():
		user = User.query.filter_by(email=form.email.data).first()
		if user is None:
			# form.email.errors.append('Email or password did not match')
			return redirect(url_for('authentication.signin'))
		elif flask_bcrypt.check_password_hash(user.password,form.password.data):
			login_user(user, form.remember_me.data)
			session['signed'] = True
			session ['username'] = user.email
			g.user = user

			if session.get('next'):
				next_page = session.get('next')
				session.pop('next')
				return redirect(url_for('portfolio.user_home'))
			else:
				return redirect(url_for('portfolio.user_home'))
		else:
			# form.password.errors.append('Email or password did not match')
			return render_template('login.html', login_form= SigninForm(), register_form=SignupForm())
	return render_template('login.html', login_form= SigninForm(), register_form=SignupForm())

@authentication.route("/logout")
@login_required
def logout():
	session.clear()
	logout_user()
	return redirect(url_for('views.index'))

@authentication.route("/register", methods=['GET','POST'])
def register():
	form = SignupForm(request.form)
	if form.validate():	

		user = User()
		form.populate_obj(user)
		user_exist = User.query.filter_by(email = form.email.data).first()
		if user_exist:
			# form.email.error.append('Email already in use.')
			return redirect(url_for('authentication.register'))

		else:
			
			user.password = flask_bcrypt.generate_password_hash(form.password.data, 15).decode('utf-8')
			user.active = True

			db.session.add(user)
			db.session.commit()
			return redirect(url_for('views.index'))
	return render_template('register.html', form=SignupForm(), login_form=SigninForm())

