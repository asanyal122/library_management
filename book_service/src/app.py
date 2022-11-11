from flask import Flask

from src.blueprints.blueprint_book import blueprint_book



app = Flask(__name__)


app.register_blueprint(blueprint_book,url_prefix='/api/v1/books')

