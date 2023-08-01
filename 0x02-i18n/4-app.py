#!/usr/bin/env python3
"""Further app set up"""

from flask_babel import Babel
from flask import request
from flask import Flask, render_template
from flask_babel import Babel
from typing import List

app = Flask(__name__)


class Config:
    """configuration class"""
    LANGUAGES: List = ["en", "fr"]
    default_locale: str = "en"
    default_timezone: str = "UTC"


app.config.from_object(Config)
babel = Babel()
babel.init_app(app)


@babel.localeselector
def get_locale() -> str:
    """get location function"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello() -> str:
    """The index html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
