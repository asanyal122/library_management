from flask import Flask
from .src.app import create_app
import os


port = int(os.environ.get('PORT', 5000))

app = create_app()
app.run(port=port)
