import os
from os import getenv
import click
from app import createApp, db
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_login import LoginManager
from app.models import User, AdminModelView

app = createApp(os.getenv('FLASK_CONFIG') or 'default')

with app.app_context():
    from app.models import Project, ProjectTag, Tag, Collab, ProjectCollab, Index, Achievement
    db.create_all()

    # admin things
    admin = Admin(app, name='MB Resume')
    admin.add_link(MenuLink(name='Public Site', category='', url=('/')))
    admin.add_view(AdminModelView(Index, db.session))
    admin.add_view(AdminModelView(Achievement, db.session))
    admin.add_view(AdminModelView(Project, db.session))
    admin.add_view(AdminModelView(Tag, db.session))
    admin.add_view(AdminModelView(Collab, db.session))


@app.shell_context_processor
def make_shell_context():
    context = app.test_request_context()
    from seed import seed_tags, seed_projects, seed_collabs, seed_index, seed_achievements
    seed_tags(db)
    seed_projects(db)
    seed_collabs(db)
    seed_achievements(db)
    seed_index(db)
    return dict(db=db, Project=Project, Tag=Tag, ProjectTag=ProjectTag, Collab=Collab, ProjectCollab=ProjectCollab, Achievement=Achievement, Index=Index)


@app.cli.command()
def deploy():
    from seed import seed_tags, seed_projects, seed_collabs, seed_index, seed_achievements
    seed_tags(db)
    seed_projects(db)
    seed_collabs(db)
    seed_achievements(db)
    seed_index(db)
    pass
