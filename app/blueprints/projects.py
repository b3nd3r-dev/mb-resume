from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Project, Tag
from app.forms import CreateProjectForm, UpdateProjectForm

projects = Blueprint('projects', __name__, template_folder='../templates')


@projects.route('/create', methods=['GET', 'POST'])
def create():
    all_tags = Tag.query.order_by(Tag.name).all()
    form = CreateProjectForm()
    form.tag_name.choices = GetTagChoices(all_tags)
    # use javascript to do what git does

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
            for tag in tags:
                new_project.tags.append(tag)  # in for loop
            db.session.add(new_project)
            db.session.commit()
            return redirect('main.index')
    else:
        print(form.errors.items())
    return render_template('projects/create.html', form=form)


@projects.route('/view/<title>')
def view(title):
    project1 = Project.query.filter_by(title=title).first()

    return render_template("project-base.html", project=project1)

    # url_for(projects.hello) for referencing projects within blueprint


@projects.route('/update', methods=['GET', 'POST'])
def update():
    all_tags = Tag.query.order_by(Tag.name).all()
    form = UpdateProjectForm()

    if form.validate_on_submit():
        new_project_name = form.name.data

        project = Project.query.filter_by(name=new_project_name).first()

        if project:
            form.populate_obj(project)
            db.session.commit()

    return render_template('projects/update.html', form=form)


def GetTagChoices(all_tags):
    tag_choices = []
    for tag in all_tags:
        tag_choices.append((tag.name.lower(), tag.name))

    return tag_choices
