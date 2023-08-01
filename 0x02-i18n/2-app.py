#!/usr/bin/env python3
"""Further app set up"""

from flask_babel import Babel
from flask import request
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


@babel.localeselector
def get_locale():
    """get location function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def hello():
    """The index html"""
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
