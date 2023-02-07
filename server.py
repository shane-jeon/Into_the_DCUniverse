"""Server for DC Universe Untitled Project App."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from jinja2 import StrictUndefined
from model import connect_to_db, db
import crud

# create the app
app = Flask(__name__)

app.secret_key = "ashen_dev"
app.jinja_env.undefined = StrictUndefined

### VIEW ###
# routing request (Telling Flask which URL should correspond with which function)
@app.route('/')
def homepage():
  """Display character names."""

  # characters = crud.get_characters()
  # character = crud.get_charID_by_name(characters.id)

  return render_template('homepage.html')


@app.route('/characters.json')
def populate_character_data():
  """Returns list of dictionaries containing all character data."""

  characters = crud.display_character_details()

  return jsonify({'characters':characters})

# Route "decorator"
@app.route('/<id>')
def characterpage(id=id):
  """View all characters."""

  character = crud.get_char_by_id(id)

  return render_template('character.html', character=character)

# condition block, Python will execute code when conditional statement evaluates to True
# Implies
if __name__ == '__main__':
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0', port=4000)