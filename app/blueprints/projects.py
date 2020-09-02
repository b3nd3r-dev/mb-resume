from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Project, Tag
from app.forms import CreateProjectForm, UpdateProjectForm, DeleteProjectForm
from sqlalchemy import func

projects = Blueprint('projects', __name__, template_folder='../templates')


@projects.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateProjectForm()

    all_tags = Tag.query.order_by(Tag.name).all()
    form.tag_name.choices = GetTagChoices(all_tags)

    if form.validate_on_submit():
        new_project_title = form.title.data
        new_project_link = form.project_link.data
        new_project_short_description = form.short_description.data
        new_project_long_description = form.long_description.data
        new_project_tags = form.tag_name.data

        project = Project.query.filter_by(title=new_project_title).first()

        if not project:
            new_project = Project(title=new_project_title,
                                  project_link=new_project_link,
                                  short_description=new_project_short_description,
                                  long_description=new_project_long_description
                                  )
            for tag in new_project_tags:
                tagtoadd = Tag.query.filter(
                    func.lower(Tag.name) == func.lower(tag)).first()
                if tagtoadd:
                    new_project.tags.append(tagtoadd)
                else:
                    flash(f"Tag { tag } does not exist")
            db.session.add(new_project)
            db.session.commit()
            flash(f"Project { new_project.title } has been created")
            return redirect(url_for('main.project'))
        else:
            flash(f"Project { project.title} already exists", "error")
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
    form = UpdateProjectForm()

    all_tags = Tag.query.order_by(Tag.name).all()
    form.tag_name.choices = GetTagChoices(all_tags)

    if form.validate_on_submit():
        new_project_title = form.title.data
        new_project_tags = form.tag_name.data

        project = Project.query.filter_by(title=new_project_title).first()

        if project:
            for tag in new_project_tags:
                tagtoadd = Tag.query.filter(
                    func.lower(Tag.name) == func.lower(tag)).first()
                if tagtoadd:
                    project.tags.append(tagtoadd)
                else:
                    flash(f"Tag { tag } does not exist")
            form.populate_obj(project)
            db.session.commit()
            flash(f"Project { project.title } has been upated")
            return redirect(url_for('main.project'))
        else:
            flash(f"Project { project.title} was not updated", "error")
    else:
        print(form.errors.items())
    return render_template('projects/update.html', form=form)


@projects.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteProjectForm()
    if form.validate_on_submit():
        project_title = form.title.data

        project = Project.query.filter_by(title=project_title).first()

        if project:
            db.session.delete(project)
            db.session.commit()
            flash(f"Project { project.title } has been deleted")
            return redirect(url_for('main.index', title=project_title))
        else:
            flash(f"Project { project_title } does not exist", "error")
    else:
        print(form.errors.items())

    return render_template('projects/delete.html', form=form)


def GetTagChoices(all_tags):
    tag_choices = []
    for tag in all_tags:
        tag_choices.append((tag.name.lower(), tag.name))

    return tag_choices
