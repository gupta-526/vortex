import os, sys
from app import login_manager
from flask_login import current_user, login_required
from app.models import *
from flask import Flask, render_template, request, Blueprint
from werkzeug.utils import secure_filename
from flask import redirect, url_for, session, current_app
# from app.cpack.circle_packing import process_fc_data, mtable_to_json

bubble = Blueprint('bubble', __name__, template_folder='../app/templates', static_folder='../app/static')

@bubble.route("/get_bubble_input/<int:proj_id>", methods=['GET','POST'])
@login_required
def get_bubble_input(proj_id):
	all_files = FileAccess.query.filter_by(p_id = proj_id).all()
	# current_proj = proj_id
	# if all_files is None:
	# 	# error = "No files uploaded yet. \n Please upload input files"
	# 	return render_template("input.html", files = all_files)

	return render_template("bubble_input.html", proj_id = proj_id, files = all_files)

@bubble.route('/bubble_viz', methods=['GET','POST'])	 
def bubble_viz():
	# filename=random_sufix()+'.txt'
	# upload_fp = os.path.join(app.config['UPLOAD_FOLDER'], upload())
	# upload_fp = upload()
	upload_fp = request.form['myFile']
	param_list = {'title': request.form['title'],
				   'fontType': request.form['fontList'],
				   'reqFile': os.path.join('static/uploads', upload_fp)}

	return render_template("bubble_viz.html", **param_list)