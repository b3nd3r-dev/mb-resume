import os
from os import getenv
import click
from app import createApp, db

from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from app.models import User, AdminModelView

app = createApp(os.getenv('FLASK_CONFIG') or 'default')


with app.app_context():
    from app.models import Project, ProjectTag, Tag, Collab, ProjectCollab
    db.create_all()

    # admin things
    admin = Admin(app, name='MB Resume')
    admin.add_view(AdminModelView(Project, db.session))
    admin.add_view(AdminModelView(Tag, db.session))
    admin.add_view(AdminModelView(Collab, db.session))


@app.shell_context_processor
def make_shell_context():
    context = app.test_request_context()
    from seed import seed_tags, seed_projects, seed_collabs
    seed_tags(db)
    seed_projects(db)
    seed_collabs(db)
    return dict(db=db, Project=Project, Tag=Tag, ProjectTag=ProjectTag, Collab=Collab, ProjectCollab=ProjectCollab)


@app.cli.command()
def deploy():
    from seed import seed_tags, seed_projects, seed_collabs
    seed_tags(db)
    seed_projects(db)
    seed_collabs(db)
    pass
