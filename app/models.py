from . import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app.utils.password import hash_password, check_password
from app import login


class Project(db.Model):
    __tablename__ = 'projects'
    # Attributes
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    project_link = db.Column(db.String, nullable=True)
    short_description = db.Column(db.Text, nullable=False)
    long_description = db.Column(db.Text, nullable=False)
    featured = db.Column(db.Boolean, default=False)

    # Relationships
    tags = relationship("Tag", secondary='project_tags',
                        back_populates='projects')

    def __init__(self, title, short_description, long_description, featured, project_link=None):
        self.title = title
        self.project_link = project_link
        self.short_description = short_description
        self.long_description = long_description
        self.featured = featured

    def __repr__(self):
        return f"Project {self.title} has {self.project_link}"


class Tag(db.Model):
    # Attributes
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    knowledge = db.Column(db.String(15), nullable=False)

    # Relationships
    projects = relationship(
        'Project', secondary='project_tags', back_populates="tags")

    def __init__(self, name, knowledge):
        self.name = name
        self.knowledge = knowledge

    def __repr__(self):
        return f"Tag {self.name}"


class ProjectTag(db.Model):
    # Attributes
    __tablename__ = "project_tags"
    project_id = db.Column(db.Integer, db.ForeignKey(
        'projects.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

    # Relationships
    # tag = relationship("Tag", backref='projects')
    # project = relationship("Project", backref='tags')

    def __init__(self, project, tag):
        self.tag = tag
        self.project = project

    def __repr__(self):
        return f"ProjectTag {self.project.title} with tag {self.tag.name}"


class User(UserMixin, db.Model):
    # Attributes
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    salt = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
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

    # def checkPassword(self, password):
    #     if password == '':
    #         return self

    #     self.password = check_password(password)

    #     return self


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
