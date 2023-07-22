#!/usr/bin/python3
""" script to start a flask web app
    - hbnb route
    - c route
    - python route
    - number route
    - number template
    - odd or even
"""

from flask import Flask, render_template


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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ print Python, with the text """
    return ("Python " + text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ return only if it's int """
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    """ render a template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """ is n odd or even """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
