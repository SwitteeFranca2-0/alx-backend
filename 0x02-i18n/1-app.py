#!/usr/bin/env python3
"""Setup the flask app"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

class Config:
    """configuration class"""
    LANGUAGES = ["en", "fr"] 
    default_locale = "en"
    default_timezone = "UTC"

app.config.from_object(Config)
babel = Babel()
babel.init_app(app)

@app.route('/')
def hello():
    """The index html"""
    return render_template(_('2-index.html'))