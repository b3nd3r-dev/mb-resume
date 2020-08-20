from flask import Blueprint, render_template, request, redirect, url_for

projects = Blueprint('projects', __name__, template_folder='../templates')

@projects.route('/')
def hello():
    return 'hello'


    # url_for(projects.hello) for referencing projects within blueprint