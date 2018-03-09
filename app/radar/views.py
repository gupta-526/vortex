import os, sys
from app import login_manager
from flask_login import current_user, login_required
from app.models import *
from app.radar.read_file import get_list
from flask import Flask, render_template, request, Blueprint
from werkzeug.utils import secure_filename
from flask import redirect, url_for, session, current_app
# from app.cpack.circle_packing import process_fc_data, mtable_to_json

radar = Blueprint('radar', __name__, template_folder='../app/templates', static_folder='../app/static')

@radar.route("/get_radar_input/<int:proj_id>", methods=['GET','POST'])
@login_required
def get_radar_input(proj_id):
	all_files = FileAccess.query.filter_by(p_id = proj_id).all()

	return render_template("radar_input.html", proj_id = proj_id, files = all_files)

@radar.route('/radar_viz', methods=['GET','POST'])	 
def radar_viz():
	legend = []
	data = []
	upload_fp = os.path.join('app/static/uploads', request.form['myFile'])
	data_dict = get_list(upload_fp)
	param_list = {'title': request.form['title'],
				   'fontType': request.form['fontList'],
				   'legend': data_dict['legend'],
				   'data': data_dict['data']}

	return render_template("radar_viz.html", **param_list)