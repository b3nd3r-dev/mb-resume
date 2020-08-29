from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Project, Tag
from app import db

projects = Blueprint('projects', __name__, template_folder='../templates')


@projects.route('/')
def hello():
    return 'hello'


@projects.route('/create/<title>/<short_description>/<long_description>')
def create(title, short_description, long_description):
    project1 = Project(title, short_description, long_description)
    db.session.add(project1)
    db.session.commmit()
    return 'create'


@projects.route('/view/<title>')
def view(title):
    project1 = Project.query.filter_by(title=title).first()

    return render_template("project-base.html", project=project1)

    # url_for(projects.hello) for referencing projects within blueprint
