# from flask import Blueprint, render_template, request, redirect, url_for, flash
# from app import db
# from app.models import Project, Collab
# from app.forms import CreateCollabForm, SearchCollabForm, UpdateCollabForm, DeleteCollabForm
# from sqlalchemy import func

# collab = Blueprint('collabs', __name__, template_folder='../templates')


# @collab.route('/create', methods=['GET', 'POST'])
# def create():
#     form = CreateCollabForm()

#     if form.validate_on_submit():
#         new_collab_fname = form.fname.data
#         new_collab_lname = form.lname.data
#         new_collab_name = form.fname.data + form.lname.data
#         new_collab_clink = form.clink.adata

#         exist = Collab.query.filter_by(name=new_collab_name).first()
#         if not exist:  # If exist returns None
#             new_collab = Collab(fname=new_collab_fname, lname=new_collab_lname, name=new_collab_name, clink=new_collab_clink)
#             db.session.add(new_collab)
#             db.session.commit()
#             flash(f"Collaborator { new_collab_fname } { new_collab_lname } has been created")
#             return redirect(url_for('main.index'))
#         else:
#             flash(f"Collaborator { new_collab_name } { new_collab_lname } already exists", "error")
#     else:
#         print(form.errors.items())
#     return render_template('collabs/create.html', form=form)


# @collab.route('/search', methods=['GET', 'POST'])
# def search():
#     form = SearchCollabForm()
#     if form.validate_on_submit():
#         collab_search_name = form.fname_search.data + form.lname_search.data
#         collab = Collab.query.filter_by(name=collab_search_name).first()
#         if collab:
#             return redirect(url_for('collabs.update', collabid=collab.id))
#         else:
#             flash(f'{collab_search_fname} + {collab_search_lname} does not exist')
#             return redirect(url_for('collabs.create'))
#     else:
#         print(form.errors.items())
#     return render_template('collabs/search.html', form=form)


# @collab.route('/update/<collabid>', methods=['GET', 'POST'])
# def update(collabid):
#     form = UpdateCollabForm()

#     if form.validate_on_submit():
#         new_collab_fname = form.fname.data
#         new_collab_lname = form.lname.data
#         new_collab_name = form.fname.data + form.lname.data
#         new_collab_clink = form.clink.data

#         exist = Collab.query.filter_by(name=new_collab_name).first()
#         if exist:
#             new_collab = Collab(fname=new_collab_fname, lname=new_collab_lname, name=new_collab_name, clink=new_collab_clink)
#             form.populate_obj(exist)
#             db.session.commit()
#             flash(f"Collaborator { new_collab_fname } { new_collab_lname } has been updated")
#             return redirect(url_for('main.index'))
#         else:
#             flash(f"Collaborator { new_collab_name } { new_collab_lname } already exists", "error")
#     else:
#         print(form.errors.items())

#     cur_collab = Collab.query.filter_by(id=collabid).first()
#     form.fname.data = cur_collab.fname
#     form.lname.data = cur_collab.lname
#     form.clink.data = cur_collab.clink
#     return render_template('collabs/update.html', form=form, collabid=collabid)


# @collab.route('/delete', methods=['GET', 'POST'])
# def delete():
#     form = DeleteCollabForm()
#     if form.validate_on_submit():
#         new_collab_name = form.fname.data + form.lname.data

#         collab = Collab.query.filter_by(name=new_collab_name).first()

#         if collab:
#             db.session.delete(collab)
#             db.session.commit()
#             flash(f'Collaborator { collab.fname } { collab.lname } has been deleted')
#             return redirect(url_for('main.index'))
#         else:
#             flash(f'Collaborator does not exist')
#             return redirect(url_for('collabs.delete'))
#     else:
#         print(form.errors.items())
#     return render_template('collabs/delete.html', form=form)
