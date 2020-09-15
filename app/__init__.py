# OS Functions
import os
from os import environ
from os.path import dirname, exists, join

from config import config

# Flask
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()


def createApp(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    config[configName].init_app(app)
    db.init_app(app)
    login.init_app(app)

    from app.blueprints.main import main as main_blueprint
    from app.blueprints.projects import projects as projects_blueprint
    from app.blueprints.tag import tag as tag_blueprint
    from app.blueprints.user import user as user_blueprint
    from app.blueprints.collab import collab as collab_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(projects_blueprint, url_prefix='/projects')
    app.register_blueprint(tag_blueprint, url_prefix='/tags')
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(collab_blueprint, url_prefix='/collabs')

    return app
