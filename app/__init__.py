"""Init for app."""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_api import FlaskAPI


DB = SQLAlchemy()

root_dir = os.path.dirname(os.path.realpath(__file__))

def create_app(config:str):
    """Set up app.

    Args:
        config (str): represent which config file we will use.
    """
    app = FlaskAPI(__name__)

    configuration = os.path.join(root_dir, 'config', str(config) + '.py')
    app.config.from_pyfile(configuration)
    app.config['SECRET_KEY'] = 'super secret key'
    DB.init_app(app)

    from app import caffe
    from app.utils import utils

    app.register_blueprint(caffe.caffe)
    app.register_blueprint(utils)

    return app
