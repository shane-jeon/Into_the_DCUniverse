"""Server for DC Universe Untitled Project App."""

from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
from model import connect_to_db

# Flask application needs to know what module to scan for, e.g., routes; required 
app = Flask(__name__)

app.secret_key = "ashen_dev"
app.jinja_env.undefined = StrictUndefined

# routing request (Telling Flask which URL should correspond with which function)
@app.route('/')
def homepage():
  """View homepage."""
  return "<div><p>Hello World!</p></div>"

# Route "decorator"
@app.route('/characters')
def characterpage():
  """View all characters."""

  return "<p>Hello characters!</p>"

# condition block, Python will execute code when conditional statement evaluates to True
# Implies
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')