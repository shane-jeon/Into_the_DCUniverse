from app import app
from flask import render_template
import crud

### VIEW ###
# routing request (Telling Flask which URL should correspond with which function)
@app.route('/')
def homepage():
  """Display character names."""

  characters = crud.get_characters()

  return render_template('index.html', characters=characters)

# Route "decorator"
@app.route('/<id>')
def characterpage(id=id):
  """View all characters."""

  character = crud.get_char_by_id(id)

  return render_template('character.html', character=character)
