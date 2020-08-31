from flask import Blueprint, redirect, render_template, request, url_for
from random import shuffle
from app import db
from app.models import Project, Tag
from app.forms import CreateTagForm, UpdateTagForm

tag = Blueprint('tags', __name__, template_folder='../templates')


@tag.route('/create', methods=['GET', 'POST'])
def create():
    form = CreateTagForm()

    all_tags = Tag.query.all()
    shuffle(all_tags)

    if form.validate_on_submit():
        new_tag_name = form.name.data
        new_tag_knowledge = form.knowledge.data

        tag_query = Tag.query.filter_by(name=new_tag_name).first()

        if not tag_query:  # If tag_query returned None
            new_tag = Tag(name=new_tag_name, knowledge=new_tag_knowledge)
            db.session.add(new_tag)
            db.session.commit()

    return render_template('tags/create.html', form=form, all_tags=all_tags)


@tag.route('/view/<tag_name>')
def view(tag_name):
    all_tags = Tag.query.all()
    shuffle(all_tags)

    tag = Tag.query.filter_by(name=tag_name).first()

    return render_template('tags/view.html', tag=tag, all_tags=all_tags)


@tag.route('/update', methods=['GET', 'POST'])
def update():
    form = UpdateTagForm()
    all_tags = Tag.query.all()
    shuffle(all_tags)

    if form.validate_on_submit():
        new_tag_name = form.name.data

        tag = Tag.query.filter_by(name=new_tag_name).first()

        if tag:
            form.populate_obj(tag)
            db.session.commit()

    return render_template('tags/update.html', form=form, all_tags=all_tags)


@tag.route('/delete/<tag_id>')
def delete(tag_id):
    pass
