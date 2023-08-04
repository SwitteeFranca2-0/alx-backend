#!/usr/bin/env python3
"""Further app set up"""

from flask_babel import Babel
from flask import request
from flask import Flask, render_template, g
from flask_babel import Babel
from typing import List
from typing import Dict, Union
import pytz
from datetime import datetime

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
    if query in app.config['LANGUAGES']:
        return query
    if g.user:
        query = g.user.get('locale')
        if query in app.config['LANGUAGES']:
            return query
    query = request.headers.get('locale')
    if query in app.config['LANGUAGES']:
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
    time = pytz.utc.localize(datetime.utcnow())
    zone_time = time.astimezone(pytz.timezone(get_timezone()))
    fmt = '%b %d, %Y, %I:%M:%S %p'
    g.time = zone_time.strftime(fmt)


def get_user() -> Union[Dict, None]:
    """get the user based on id"""
    query = request.args.get('login_as')
    if query is not None and int(query) in users.keys():
        return users.get(int(query))
    return None


@babel.timezoneselector
def get_timezone() -> str:
    query = request.args.get('timezone')
    try:
        return pytz.timezone(query).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    query = g.user.get('timezone')
    try:
        return pytz.timezone(query).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def hello() -> str:
    """The index html"""
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
