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
def display_ctext(text_to_display):
    """
    display “C ” followed by the value of the text
    """
    return "C {}".format(text_to_display.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text_to_display="is cool"):
    """
    display python is cool
    """
    return "Python {}".format(text_to_display.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
