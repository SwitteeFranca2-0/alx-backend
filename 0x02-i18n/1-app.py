#!/usr/bin/env python3
"""Setup the flask app"""

from flask import Flask, render_template
from flask_babel import Babel
from typing import List

app = Flask(__name__)


class Config:
    """configuration class"""
    LANGUAGES: List = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)
babel = Babel()
babel.init_app(app)


@app.route('/', strict_slashes=False)
def hello() -> str:
    """The index html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
