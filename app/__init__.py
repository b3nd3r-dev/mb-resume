# OS Functions
import os
from os import environ
from os.path import dirname, exists, join

import logging
from logging.handlers import RotatingFileHandler

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

   

    if not app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/resume.log', maxBytes=10240,
                                        backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Resume Startup')
    

    # Other Setup
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)

    from app.blueprints.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    return app


def create_admin(app=None):
    return Admin(app, template_mode='bootstrap3')
