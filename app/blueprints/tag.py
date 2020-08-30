from flask import Blueprint, redirect, render_template, request, url_for

from app import db
from app.models import Project, Tag
from app.forms import CreateTagForm

tag = Blueprint('tags', __name__, template_folder='../templates')


@tag.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateTagForm()

    if form.validate_on_submit():
        new_tag_name = form.name.data
        new_tag_knowledge = form.knowledge.data

        tag_query = Tag.query.filter_by(name=new_tag_name).first()

        if not tag_query:  # If tag_query returned None
            new_tag = Tag(name=new_tag_name, knowledge=new_tag_knowledge)
            db.session.add(new_tag)
            db.session.commit()

    return render_template('tags/create.html', form=form)
    pass


@tag.route('/view/<tag_id>')
def view(tag_id):
    pass


@tag.route('/update/<tag_id>')
def update(tag_id):
    pass


@tag.route('/delete/<tag_id>')
def delete(tag_id):
    pass
