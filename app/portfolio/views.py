import json, os, string
from flask_login import current_user, login_required
from app.models import *
from app.portfolio.forms import *
from flask import Flask, render_template, request, Blueprint
from werkzeug.utils import secure_filename
from flask import redirect, url_for, session, current_app
from app import login_manager


portfolio = Blueprint('portfolio', __name__, template_folder='../app/templates', static_folder='../app/static')

@portfolio.route('/home', methods=['GET','POST'])
@login_required
def user_home():
    if current_user.is_authenticated:
        c_id = current_user.id
        all_proj = UserAccess.query.filter_by(user_id = c_id).all()
        error = None
        if all_proj is None:
            error = "No projects created"
            return render_template('user_page.html', error = error)
        all_files = {project.Project.id: get_files(project.Project.id) for project in all_proj}


    return render_template('user_page.html', all_proj = all_proj, 
                add_proj=ProjectForm(), add_file=FileForm(), all_files=all_files)


def get_files(proj_id):
    if current_user.is_authenticated:
        all_files = FileAccess.query.filter_by(p_id = proj_id).all()
        error = None
        if all_files is None:
            error = "No files uploaded yet"
            return error
    return all_files


@portfolio.route('/add_project', methods=['GET','POST'])
@login_required
def add_project():
    form = ProjectForm(request.form)

    if form.validate():
        result = {}
        result['iserror'] = False

        if form.project_id.data is not None:
            if current_user is not None:
                userid=current_user.id
                project=Project(project_name=form.name.data, description=form.description.data)
                db.session.add(project)
                db.session.commit()
                user_access = UserAccess(user_id=current_user.id, project_id=project.id, can_edit=True)
                db.session.add(user_access)
                db.session.commit()
                result['savedsuccess'] = True
            else:
                result['savedsuccess'] = False
        else:
            portfolio = Portfolio.query.get(form.portfolio_id.data)
            form.populate_obj(portfolio)
            db.session.commit()
            result['savedsuccess'] = True

        return json.dumps(result)

    form.errors['iserror'] = True
    print(form.errors)
    return json.dumps(form.errors)



@portfolio.route('/delete_project/<int:proj_id>')
@login_required
def delete_project(proj_id):
    proj = Project.query.get(proj_id)
    usr_acc = UserAccess.query.filter_by(user_id = current_user.id, project_id = proj_id).first()
    db.session.delete(usr_acc)
    db.session.commit()
    db.session.delete(proj)
    db.session.commit()
    result = {}
    result['sucess'] = True
    return json.dumps(result)

@portfolio.route('/random_sufix',methods=['GET','POST'])
def random_sufix(length=6, chars=string.ascii_uppercase+string.digits):
    return ''.join([random.choice(chars) for _ in range(length)])


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in (current_app.config['ALLOWED_EXTENSIONS'])

@portfolio.route('/add_file/<int:proj_id>', methods=['GET','POST'])
@login_required
def add_file(proj_id):
    result = {}
    if request.method == 'POST':
        # id = request.form["file"]
        file = request.files['file']
        result['savedsuccess'] = False
        if file and allowed_file(str.lower(str(file.filename))):
            filename = secure_filename(file.filename)
            filename_save = filename+"_"+str(proj_id)
    
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename) )
            file_uploaded = File(uploaded_file=filename) 
            db.session.add(file_uploaded)
            db.session.commit()
            
            file_acc = FileAccess(file_id=file_uploaded.id, p_id=proj_id)
            db.session.add(file_acc)
            db.session.commit()
            
            result['savedsuccess'] = True  
    return json.dumps(result)



@portfolio.route('/delete_file/<int:proj_id>')
@login_required
def delete_file(self, proj_id):
    # file_td = 
    File.query.filter_by(id=proj_id).delete()
    db.session.delete(file_td)
    db.session.commit()
    result = {}
    result['result'] = 'success'
    return json.dumps(result)

@portfolio.route('/create_viz/<int:proj_id>')
@login_required
def create_viz(proj_id):
    return render_template('create_viz.html', proj_id = proj_id)
