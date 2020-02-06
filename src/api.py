from flask import Flask
from flask_restful import Api
from src import routes
from src.models import db


def get_app(config_filename='config'):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    return app


def run_local_api():
    app = get_app()
    api = Api(app)

    db.init_app(app)

    routes.setup(api)

    return app.run(debug=True)
