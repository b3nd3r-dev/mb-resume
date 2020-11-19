from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, SelectMultipleField, TextAreaField

from wtforms.fields.html5 import EmailField
# from app.models import Tag, Collab
from wtforms.validators import DataRequired, EqualTo, Email, Length


# --------------- TAGS ---------------

tag_choices = [
    ('fluent', 'Fluent'),
    ('proficient', 'Proficient'),
    ('familiar', 'Familiar')
]


class CreateTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])
    knowledge = SelectField('What\'s your Proficiency', choices=tag_choices)
    submit = SubmitField('Create Tag')


class UpdateTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])
    knowledge = SelectField('What\'s your Proficiency', choices=tag_choices)
    submit = SubmitField('Update Tag')


class DeleteTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])
    submit = SubmitField('Delete Tag')

# --------------- PROJECTS ---------------


class CreateProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    project_link = StringField('Project Link')
    short_description = TextAreaField("Short Description")
    long_description = TextAreaField("Long Description")
    tag_name = SelectMultipleField('Tag Name')
    collab_name = SelectMultipleField('Collaborator Name')
    featured = BooleanField('Featured:')
    submit = SubmitField('Create Project')


class SearchProjectForm(FlaskForm):
    title_search = StringField(
        "Search for project", validators=[DataRequired()])
    search = SubmitField('Search')


class UpdateProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    project_link = StringField('Project Link')
    short_description = TextAreaField("Short Description")
    long_description = TextAreaField("Long Description")
    tag_name = SelectMultipleField('Tag Name')
    collab_name = SelectMultipleField('Collaborator Name')
    featured = BooleanField('Featured:')
    submit = SubmitField('Update Project')


class DeleteProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    submit = SubmitField('Delete Project')

# --------------- USERS ---------------


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirm_p', message="Passwords must match"),
        Length(min=8, max=24, message="Password must be 8 characters")])
    confirm_p = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# --------------- COLABS ---------------


class CreateCollabForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    clink = StringField('Collaborator Link')
    submit = SubmitField('Create Collaborator')


class SearchCollabForm(FlaskForm):
    fname_search = StringField("First name", validators=[DataRequired()])
    lname_search = StringField("Last Name", validators=[DataRequired()])
    search = SubmitField('Search')


class UpdateCollabForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    clink = StringField('Collaborator Link')
    submit = SubmitField('Update Collaborator')


class DeleteCollabForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Delete Collaborator')
