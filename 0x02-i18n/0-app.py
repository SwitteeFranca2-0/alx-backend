#!/usr/bin/env python3
"""Setup the flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello() -> str:
    """The index html"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
