#!/usr/bin/python3
"""
Starts a flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    returns the below string
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    returns HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_ctext():
    """
    display “C ” followed by the value of the text
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
