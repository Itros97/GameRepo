# flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


from DatabaseInfo import app_config
# db variable initialization
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("/home/inigo/GameRepo/DatabaseInfo/config.json")
    db.init_app(app)

    return app
