from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Project, Tag
from app import db
from app.forms import CreateProjectForm

projects = Blueprint('projects', __name__, template_folder='../templates')


@projects.route('/')
def hello():
    return 'hello'


@projects.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateProjectForm()

    if form.validate_on_submit():
        new_project_title = form.title.data
        new_project_link = form.link.data
        new_project_short_description = form.short_description.data
        new_project_long_description = form.long_description.data

        project = Project.query.filter_by(title=new_project_title).first()

        if not project:
            new_project = Project(title=new_project_title,
                                  project_link=new_project_link,
                                  short_description=new_project_short_description,
                                  long_description=new_project_long_description
                                  )
            db.session.add(new_project)
            db.session.commit()

    return render_template('projects/create.html', form=form)


@projects.route('/view/<title>')
def view(title):
    project1 = Project.query.filter_by(title=title).first()

    return render_template("project-base.html", project=project1)

    # url_for(projects.hello) for referencing projects within blueprint
