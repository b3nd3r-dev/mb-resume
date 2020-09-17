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
            new_password = form.password.data

            user_exist_username = User.query.filter_by(username=new_username).first()

            # if user does not exist
            if not user_exist_username:
                new_user = User(username=new_username,
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
