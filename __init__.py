from flask import Flask
from flask_restful import Api

import models
from models import db


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///data/dat.db'
    )

    models.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app
