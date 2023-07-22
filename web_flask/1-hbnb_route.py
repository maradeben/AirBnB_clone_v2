#!/usr/bin/python3
""" script to start a flask web app, adding the /hbnb route """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hello():
    """ print 'Hello HBNB' """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ print 'HBNB' """
    return ("HBNB")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
