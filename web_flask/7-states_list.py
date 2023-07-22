#!/usr/bin/python3
""" script that starts Flask web app
fetches data from storage
displays information on states
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def show_states(states_list):
    """ query database and pass states to render """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def teardown(exc):
    """ remove current SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
