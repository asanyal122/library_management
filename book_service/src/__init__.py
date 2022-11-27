from flask import Flask
from .blueprints.blueprint_book import blueprint_book


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint_book,url_prefix='/api/v1/books')
    return app