#OS Functions
import os
from os import environ                                                      
from os.path import dirname, exists, join                                   

from config import config 

#Flask
from flask import Flask, redirect, render_template, request, url_for

def createApp(configName):
    app = Flask(__name__)
    app.config.from_object(config[configName])
    config[configName].init_app(app)

    from app.blueprints.main import main as main_blueprint
    from app.blueprints.projects import projects as projects_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(projects_blueprint, url_prefix='/projects')

    return app
