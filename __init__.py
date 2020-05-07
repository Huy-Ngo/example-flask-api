from flask import Flask
import models


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///data/dat.db'
    )

    models.init_app(app)

    return app
