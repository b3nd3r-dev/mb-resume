# from flask import Blueprint, render_template, request, redirect, url_for, flash
# from app import db
# from app.models import Project, Tag, Collab
# from app.forms import CreateProjectForm, SearchProjectForm, UpdateProjectForm, DeleteProjectForm
# from sqlalchemy import func

# projects = Blueprint('projects', __name__, template_folder='../templates')


# @projects.route('/create', methods=['GET', 'POST'])
# def create():
#     form = CreateProjectForm()

#     all_tags = Tag.query.order_by(Tag.name).all()
#     form.tag_name.choices = GetTagChoices(all_tags)

#     all_collabs = Collab.query.order_by(Collab.name).all()
#     form.collab_name.choices = GetCollabChoices(all_collabs)

#     feat_proj = Project.query.filter_by(featured=True).all()

#     if form.validate_on_submit():
#         new_project_title = form.title.data
#         new_project_link = form.project_link.data
#         new_project_short_description = form.short_description.data
#         new_project_long_description = form.long_description.data
#         new_project_featured = form.featured.data
#         new_project_tags = form.tag_name.data
#         new_project_collabs = form.collab_name.data

#         project = Project.query.filter_by(title=new_project_title).first()

#         if not project:
#             # ONLY 6 FEATURED PROJECTS ALLOWED
#             if ((len(feat_proj)) > 5) and (new_project_featured == True):
#                 flash('There can only be 6 featured projects', 'error')
#                 return render_template('projects/create.html', form=form)

#             else:
#                 new_project = Project(title=new_project_title,
#                                       project_link=new_project_link,
#                                       short_description=new_project_short_description,
#                                       long_description=new_project_long_description,
#                                       featured=new_project_featured
#                                       )
#                 # APPENDING TAGS TO PROJECT
#                 for tag in new_project_tags:
#                     tagtoadd = Tag.query.filter(
#                         func.lower(Tag.name) == func.lower(tag)).first()
#                     if tagtoadd:
#                         new_project.tags.append(tagtoadd)
#                     else:
#                         flash(f"Tag { tag } does not exist")

#                 # APPENDING COLLABS TO PROJECT
#                 for collab in new_project_collabs:
#                     collabtoadd = Collab.query.filter(func.lower(Collab.name) == collab).first()
#                     if collabtoadd:
#                         new_project.collabs.append(collabtoadd)
#                     else:
#                         flash(f"Collaborator { collab } does not exist")
#                         return render_template('projects/create.html', form=form)

#                 db.session.add(new_project)
#                 db.session.commit()
#                 flash(f"Project { new_project.title } has been created")
#                 return redirect(url_for('main.project'))
#         else:
#             flash(f"Project { project.title} already exists", "error")
#     else:
#         print(form.errors.items())
#     return render_template('projects/create.html', form=form)


# @ projects.route('/view/<title>')
# def view(title):
#     project1 = Project.query.filter_by(title=title).first()

#     return render_template("project-base.html", project=project1)

#     # url_for(projects.hello) for referencing projects within blueprint


# @ projects.route('/search', methods=['GET', 'POST'])
# def search():
#     form = SearchProjectForm()
#     if form.validate_on_submit():
#         project_search_title = form.title_search.data
#         project = Project.query.filter_by(title=project_search_title).first()
#         if project:
#             return redirect(url_for('projects.update', projectid=project.id))
#         else:
#             flash(f'{project_search_title} does not exist')
#             return redirect(url_for('projects.cre'))
#     else:
#         print(form.errors.items())
#     return render_template('projects/search.html', form=form)


# @ projects.route('/update/<projectid>', methods=['GET', 'POST'])
# def update(projectid):
#     form = UpdateProjectForm()

#     all_tags = Tag.query.order_by(Tag.name).all()
#     form.tag_name.choices = GetTagChoices(all_tags)

#     all_collabs = Collab.query.order_by(Collab.name).all()
#     form.collab_name.choices = GetCollabChoices(all_collabs)

#     if form.validate_on_submit():
#         new_project_title = form.title.data
#         new_project_tags = form.tag_name.data
#         new_project_collabs = form.collab_name.data

#         project = Project.query.filter_by(title=new_project_title).first()

#         if project:
#             # APPENDING TAGS TO PROJECT
#             for tag in new_project_tags:
#                 tagtoadd = Tag.query.filter(func.lower(Tag.name) == func.lower(tag)).first()
#                 if tagtoadd:
#                     project.tags.append(tagtoadd)
#                 else:
#                     flash(f"Tag { tag } does not exist")
#             # APPENDING COLLABS TO PROJECT
#             for collab in new_project_collabs:
#                 collabtoadd = Collab.query.filter(func.lower(Collab.name) == collab).first()
#                 if collabtoadd:
#                     project.collabs.append(collabtoadd)
#                 else:
#                     flash(f"Collaborator { collab } does not exist")
#                     return render_template('projects/create.html', form=form)
#             form.populate_obj(project)
#             db.session.commit()
#             flash(f"Project { project.title } has been upated")
#             return redirect(url_for('main.project'))
#         else:
#             flash(f"Project { project.title} was not updated", "error")
#     else:
#         print(form.errors.items())

#     # query tag list for tags already attached

#     cur_proj = Project.query.filter_by(id=projectid).first()
#     print('this thing here')
#     print(cur_proj.tags)
#     print(type(cur_proj.tags))

#     # Initial : User -> View -> Form Gets updated from DB -> If Post or If Get this was with the cur project grabs at the top of function
#     # POST : User -> View -> POSTING (DON'T UPDATE FORM) -> Update Object
#     # GET : User -> View -> NO POST -> Populate data from database -> Render template

#     # Initial data from passed project ID rendered to template
#     form.title.data = cur_proj.title
#     form.short_description.data = cur_proj.short_description
#     form.long_description.data = cur_proj.long_description
#     form.featured.data = cur_proj.featured
#     form.project_link.data = cur_proj.project_link

#     form.tag_name.data = cur_proj.tags
#     form.collab_name.data = cur_proj.collabs
#     return render_template('projects/update.html', form=form, projectid=projectid)


# @ projects.route('/delete', methods=['GET', 'POST'])
# def delete():
#     form = DeleteProjectForm()

#     if form.validate_on_submit():
#         project_title = form.title.data

#         project = Project.query.filter_by(title=project_title).first()

#         if project:
#             db.session.delete(project)
#             db.session.commit()
#             flash(f"Project { project.title } has been deleted")
#             return redirect(url_for('main.index', title=project_title))
#         else:
#             flash(f"Project { project_title } does not exist", "error")
#     else:
#         print(form.errors.items())

#     return render_template('projects/delete.html', form=form)


# def GetTagChoices(all_tags):
#     tag_choices = []
#     for tag in all_tags:
#         tag_choices.append((tag.name.lower(), tag.name))

#     return tag_choices


# def GetCollabChoices(all_collabs):
#     collab_choices = []
#     for collab in all_collabs:
#         collab_choices.append((collab.name.lower(), collab.name))

#     return collab_choices


# def FilterTagChoices(all_tags, cur_tags):
#     filter_tag_choices = []
#     print(type(cur_tags))
#     for tag in all_tags:
#         tagss = Tag.query.filter_by(name == (tag.name.lower(), tag.name)).first()
#         print(tagss)
#         # if tagss:
#         #     filter_tag_choices.append(tag)
#         # else:
#         #     pass
#     return filter_tag_choices
