import os
from os import getenv
import click
from app import createApp

app = createApp(os.getenv('FLASK_CONFIG') or 'default')

@app.cli.command()
def deploy():
    pass