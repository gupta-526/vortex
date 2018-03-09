# file to handle backend functions of circle packing vizualization
import os, sys
from app import login_manager
from flask_login import current_user, login_required
from app.models import *
from flask import Flask, render_template, request, Blueprint
from werkzeug.utils import secure_filename
from flask import redirect, url_for, session, current_app
from app.cpack.circle_packing import process_fc_data, mtable_to_json

cpack = Blueprint('cpack', __name__, template_folder='../app/templates', static_folder='../app/static')
# current_proj = 0


@cpack.route("/cpackModelType", methods= ['GET','POST'])
def cpackModelType():
	imageType = request.form['imageType']
	fname = request.form['myFiles']
	print(fname)
	filename = os.path.join('app/static/uploads/', fname)
	print(filename)
	output_fname = fname.split('.')[0]+'.json'
	print(output_fname)
	process_fc_data(filename, os.path.join('app/static/uploads/', output_fname))
	param_list = {'title': request.form['title'],
				   'subA':request.form['subjectA'],
				   'subB':request.form['subjectB'],
				   'fc_limit':request.form['nLimit'],
				   'nColor':request.form['nColor'],
				   'fillColor':request.form['fColor'],
				   'colorA':request.form['aColor'],
				   'colorB':request.form['bColor'],
				   'opacityRoot':request.form['opacity'],
				   'fontType':request.form['fontList'],
				   'fSize':request.form['fsize'],
				   'reqFile': os.path.join('static/uploads/',output_fname) }
				   
	if(imageType=='simple'):
		
		return render_template("cpack_viz.html", **param_list)
		
	elif(imageType=='zoomable'):
	  
		return render_template("zoomable.html", **param_list)

@cpack.route("/get_input/<int:proj_id>", methods=['GET','POST'])
@login_required
def get_input(proj_id):
	all_files = FileAccess.query.filter_by(p_id = proj_id).all()
	# current_proj = proj_id
	# if all_files is None:
	# 	# error = "No files uploaded yet. \n Please upload input files"
	# 	return render_template("input.html", files = all_files)


	return render_template("input.html", proj_id = proj_id, files = all_files)

