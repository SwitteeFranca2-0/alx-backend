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
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """get location function"""
    queries = request.query_string.decode('utf-8').split("&")
    query_dict = {}
    for query in queries:
        if "=" in query:
            arg = query
        else:
            arg = "0=" + query
        args = arg.split("=")
        query_dict[args[0]] = args[1]
    if "locale" in query_dict:
        if query_dict["locale"] in app.config['LANGUAGES']:    
            return query_dict["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello() -> str:
    """The index html"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
