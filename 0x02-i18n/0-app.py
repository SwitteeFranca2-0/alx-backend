#!/usr/bin/env python3
"""Setup the flask app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    """The index html"""
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)