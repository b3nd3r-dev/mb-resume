from . import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin, current_user
from app.utils.password import hash_password, check_password
from app import login
from flask_admin.contrib.sqla import ModelView


class Project(db.Model):
    __tablename__ = 'projects'
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    project_link = db.Column(db.String, nullable=True)
    short_description = db.Column(db.UnicodeText)
    long_description = db.Column(db.UnicodeText)
    featured = db.Column(db.Boolean, default=False)

    # Relationships
    tags = relationship("Tag", secondary='project_tags',
                        backref=db.backref('projects', lazy='dynamic'))
    achievements = relationship("Achievement", secondary='achievement_projects',
                        backref=db.backref('projects', lazy='joined'))
    collabs = relationship("Collab", secondary='project_collabs',
                           back_populates='projects')

    def __init__(self, title, short_description, long_description, featured, project_link=None):
        self.title = title
        self.project_link = project_link
        self.short_description = short_description
        self.long_description = long_description
        self.featured = featured

    def __repr__(self):
        return f"{self.title}"


class Tag(db.Model):
    # Attributes
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(28), unique=True, nullable=False)
    knowledge = db.Column(db.String(15), nullable=False)
    show_on_front = db.Column(db.Boolean)

    def __init__(self, name, knowledge, show_on_front=True):
        self.name = name
        self.knowledge = knowledge
        self.show_on_front = show_on_front

    def __repr__(self):
        return f"{self.name}"


class ProjectTag(db.Model):
    # Attributes
    __tablename__ = "project_tags"
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

    # Relationships
    tag = db.relationship('Tag', backref=db.backref('projtags', lazy='joined',  cascade="all, delete-orphan"))
    project = db.relationship('Project', backref=db.backref('projtags', lazy='joined',  cascade="all, delete-orphan"))
    # tag = relationship("Tag", backref='projects')
    # project = relationship("Project", backref='tags')

    def __init__(self, project, tag, show_on_front=True):
        self.tag = tag
        self.project = project
        self.show_on_front = show_on_front

    def __unicode__(self):
        return f"ProjectTag {self.project.title} with tag {self.tag.name}"

    def __repr__(self):
        return f"ProjectTag {self.project.title} with tag {self.tag.name}"


class Collab(db.Model):
    __tablename__ = 'collabs'
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30), nullable=False)
    lname = db.Column(db.String(30), nullable=False)
    clink = db.Column(db.String, nullable=True)
    name = fname + ' ' + lname

    # Relationships
    projects = relationship(
        'Project', secondary='project_collabs', back_populates="collabs")

    def __init__(self, fname, lname, name, clink=None):
        self.fname = fname
        self.lname = lname
        self.name = name

    def __repr__(self):
        return f"{self.fname} {self.lname}"


class ProjectCollab(db.Model):
    # Attributes
    __tablename__ = "project_collabs"
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    collab_id = db.Column(db.Integer, db.ForeignKey('collabs.id'), primary_key=True)

    def __init__(self, project, collab):
        self.collab = collab
        self.project = project

    def __repr__(self):
        return f"ProjectTag {self.project.title} with collab {self.collab.fname}"


class User(UserMixin, db.Model):
    # Attributes
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(128), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.setPassword(password)
        pass

    def setPassword(self, password):
        if password == '':
            return self

        # Returns <hashed_password>:<salt>
        hashedPassword = hash_password(password)

        # Returns [<hashed_password>, <salt>]
        splitPassword = hashedPassword.split(':')

        self.password_hash = splitPassword[0]  # <hashed_password>
        self.salt = splitPassword[1]  # <salt>

        return self


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class AboutMe(db.Model):
    __tablename__ = 'AboutMes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    subtitle = db.Column(db.String)
    description = db.Column(db.Text)
    quote = db.Column(db.Text)

    def __init__(self, title, subtitle, description, quote):
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.quote = quote

    def __repr__(self):
        return f"{self.title}"


class Achievement(db.Model):
    __tablename__ = 'achievements'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    desc = db.Column(db.Text)
    link = db.Column(db.String)
    link_name = db.Column(db.String)
    icon = db.Column(db.String, nullable=False)
    order = db.Column(db.Integer, nullable=False, default=1)


    def __init__(self, name, start_date, end_date, desc, link, link_name, icon, order=1):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.desc = desc
        self.link = link
        self.link_name = link_name
        self.icon = icon
        self.order = order

    def __repr__(self):
        return f"{self.name}"

class AchievementProject(db.Model):
    # Attributes
    __tablename__ = "achievement_projects"
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), primary_key=True)
    achievement_id = db.Column(db.Integer, db.ForeignKey('achievements.id'), primary_key=True)

    # Relationships
    # achievement = db.relationship('Achievement', backref=db.backref('achivprojects', lazy='dynamic'))
    # project = db.relationship('Project', backref=db.backref('achivprojects', lazy='dynamic'))
    # tag = relationship("Tag", backref='projects')
    # project = relationship("Project", backref='tags')

    def __init__(self, project, achievement):
        self.achievement = achievement
        self.project = project