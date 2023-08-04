#!/usr/bin/env python3
"""Further app set up"""

from flask_babel import Babel
from flask import request
from flask import Flask, render_template, g
from flask_babel import Babel
from typing import List
from typing import Dict, Union

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
    query = request.args.get('locale')
    if query is not None and query in app.config['LANGUAGES']:
        return query
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request() -> None:
    """Perfoem some things before getting user"""
    g.user = get_user()


def get_user() -> Union[Dict, None]:
    """get the user based on id"""
    query = request.args.get('login_as')
    if query is not None and int(query) in users.keys():
        return users.get(int(query))
    return None


@app.route('/', strict_slashes=False)
def hello() -> str:
    """The index html"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
