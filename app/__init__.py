# OS Functions
import os
from os import environ
from os.path import dirname, exists, join

from config import config

# Flask
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()


def createApp(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    config[configName].init_app(app)
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    from app.blueprints.main import main as main_blueprint
    from app.blueprints.user import user as user_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint, url_prefix='/users')

    return app


def create_admin(app=None):
    return Admin(app, template_mode='bootstrap3')
