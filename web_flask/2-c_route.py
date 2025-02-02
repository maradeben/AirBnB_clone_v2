#!/usr/bin/python3
""" script to start a flask web app
    - hbnb route
    - c route
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ print 'Hello HBNB' """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ print 'HBNB' """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ print C, with the text passed in """
    return ("C " + text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
