from flask import Blueprint, redirect, render_template, request, url_for, flash
from app import db
from app.models import User
from app.forms import RegisterForm, LoginForm
from flask_login import current_user, login_user, logout_user
from app.utils.password import check_password

user = Blueprint('user', __name__, template_folder='../templates/users')


@user.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegisterForm()
        return render_template('register.html', form=form)

    elif request.method == 'POST':
        form = RegisterForm()

        if form.validate():

            new_username = form.username.data
            new_email = form.email.data
            new_password = form.password.data

            user_exist_username = User.query.filter_by(username=new_username).first()
            user_exist_email = User.query.filter_by(email=new_email).first()

            # if user does not exist
            if not user_exist_username and not user_exist_email:
                new_user = User(username=new_username,
                                email=new_email,
                                password=new_password
                                )
                db.session.add(new_user)
                db.session.commit()
            # if user already exists
            else:
                flash(f"{ new_username} already exists, please choose a new user")
                return redirect(url_for("user.register"))
        # form did not validate
        else:
            flash("Validation Error on Forms, see below")
            return render_template('register.html', form=form)

        return redirect(url_for("main.index"))


@ user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.login"))

    # if request.method == 'GET':
    #     loginForm = LoginForm()
    #     if request.args.get('next') is not None:
    #         loginForm.nextURL.data = request.args['next']

    else:
        form = LoginForm()

        if form.validate_on_submit():

            user = User.query.filter_by(username=form.username.data).first()

            if user and check_password(user, form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect(url_for("main.index"))

            else:
                flash('Invalid username or password', 'error')
                return redirect(url_for("main.login"))

        return render_template('login.html', form=form)


@ user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@ user.route('/update', methods=['GET', 'POST'])
def update():
    pass


@ user.route('/delete', methods=['GET', 'POST'])
def delete():
    pass
