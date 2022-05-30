import os
from os import getenv
import click
from app import createApp, db
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_login import LoginManager
from app.models import User
from wtforms import TextAreaField
from wtforms.widgets import TextArea
from flask_admin.contrib.sqla import ModelView
from flask_migrate import upgrade


app = createApp(os.getenv('FLASK_CONFIG') or 'default')

class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class WYSIWYGModelView(ModelView):
    form_overrides = dict(description=CKTextAreaField, quote=CKTextAreaField, desc=CKTextAreaField, short_description=CKTextAreaField, long_description=CKTextAreaField)

    create_template = 'edit.html'
    edit_template = 'edit.html'

    def is_accessible(self):
        from flask_login import current_user
        return current_user.is_authenticated


with app.app_context():
    from app.models import Project, ProjectTag, Tag, Collab, ProjectCollab, AboutMe, Achievement

    # admin things
    admin = Admin(app, name='MB Resume')
    admin.add_link(MenuLink(name='Public Site', category='', url=('/')))
    admin.add_view(WYSIWYGModelView(AboutMe, db.session))
    admin.add_view(WYSIWYGModelView(Achievement, db.session))
    admin.add_view(WYSIWYGModelView(Project, db.session))
    admin.add_view(WYSIWYGModelView(Tag, db.session))
    admin.add_view(WYSIWYGModelView(Collab, db.session))


@app.shell_context_processor
def make_shell_context():
    import pdfkit
    from flask import render_template
    ctx = app.test_request_context('/nothing')
    ctx.push()
    context = app.test_request_context()

    if not app.config['DEBUG'] and not app.config['TESTING']:
        from app.seed import seed_tags, seed_projects, seed_collabs, seed_aboutme, seed_achievements
        seed_tags(db)
        seed_projects(db)
        seed_collabs(db)
        seed_achievements(db)
        seed_aboutme(db)

    aboutmes = AboutMe.query.all()
    achievements = Achievement.query.all()
    projects = Project.query.all()
    
    return dict(db=db, Project=Project, Tag=Tag, ProjectTag=ProjectTag, Collab=Collab, ProjectCollab=ProjectCollab, Achievement=Achievement, AboutMe=AboutMe)


@app.cli.command()
def deploy():
    upgrade()


    if not os.getenv('FLASK_CONFIG').lower() == 'production':
        from app.seed import seed_tags, seed_projects, seed_collabs, seed_aboutme, seed_achievements, seed_users
        seed_tags(db)
        seed_projects(db)
        seed_collabs(db)
        seed_achievements(db)
        seed_aboutme(db)
        seed_users(db)

    pass
