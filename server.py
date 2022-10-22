"""Server for DC Universe Untitled Project App."""

from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined


app = Flask(__name__)

app.secret_key = "ashen_dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
  """View homepage."""
  return "<div><p>Hello World!</p></div>"

@app.route('/characters')
def characterpage():
  """View all characters."""

  return "<p>Hello characters!</p>"