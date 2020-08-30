from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

tag_choices = [
    ('fluent', 'Fluent'),
    ('proficient', 'Proficient'),
    ('familiar', 'Familiar')
]


class CreateTagForm(FlaskForm):
    name = StringField('Tag Name', validators=[DataRequired()])
    knowledge = SelectField('What\'s your Proficiency', choices=tag_choices)
    submit = SubmitField('Create Tag')
