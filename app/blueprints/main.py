from random import shuffle

from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import logout_user, login_user, current_user
from app import db
from app.models import Project, Tag, User
from app.forms import LoginForm
from app.utils.password import check_password

main = Blueprint('main', __name__, template_folder='../templates')


def chunks(lst, n):
    # """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


@main.route('/')
def index():
    # Project Splitting
    feat_proj = Project.query.filter_by(featured=True).all()
    print(len(feat_proj))
    if len(feat_proj) > 6:
        flash('There can only be 6 featured projects, please correct on update page')
        return redirect(url_for('main.project'))
    else:
        split_project_list = list(chunks(feat_proj, int(len(feat_proj) / 2)))
        first_project_list = split_project_list[0]
        second_project_list = split_project_list[1]

        if len(split_project_list) > 2:
            first_project_list.extend(split_project_list[2])

        # Query all Tags and Shuffle the output
        all_tags = Tag.query.all()
        shuffle(all_tags)

        # Split tags into 3 different lists
        # https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
        split_tag_list = list(chunks(all_tags, int(len(all_tags) / 3)))

        first_tag_list = split_tag_list[0]
        second_tag_list = split_tag_list[1]
        third_tag_list = split_tag_list[2]

        if len(split_tag_list) > 3:
            third_tag_list.extend(split_tag_list[3])

    return render_template('index.html',
                           first_tag_list=first_tag_list,
                           second_tag_list=second_tag_list,
                           third_tag_list=third_tag_list,
                           first_project_list=first_project_list,
                           second_project_list=second_project_list
                           )


@ main.route('/project')
def project():
    all_projects = Project.query.all()
    all_projects.reverse()
    split_project_list = list(chunks(all_projects, int(len(all_projects) / 2)))

    first_project_list = split_project_list[0]
    second_project_list = split_project_list[1]

    if len(split_project_list) > 2:
        first_project_list.extend(split_project_list[2])

    # if len(first_project_list) > 3 or len(second_project_list) > 3:
    #     flash(f'You can only have 6 featured projects, please update one before continuing')
    #     return redirect(url_for('project.update'))
    return render_template('project.html',
                           all_projects=all_projects,
                           first_project_list=first_project_list,
                           second_project_list=second_project_list
                           )


@ main.route('/projectdetail/<projectid>')
def projectdetail(projectid):
    project = Project.query.filter_by(id=projectid).first()
    return render_template('project-detail-base.html', project=project)


@ main.route('/tagdetail/<tagid>')
def tagdetail(tagid):
    project = Project.query.all()
    tag = Tag.query.filter_by(id=tagid).first()
    return render_template('tag-base.html', tag=tag, project=project)


@ main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already logged in')
        return redirect(url_for("main.index"))

    else:
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()

            if user and check_password(user, form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect('/admin')

            else:
                flash('Invalid username or password', 'error')
                return redirect(url_for("main.index"))

    return render_template('login.html', form=form)


@main.route('/logout')
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('main.index'))
