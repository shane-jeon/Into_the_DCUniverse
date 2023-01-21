from app import app
from flask import render_template, request, jsonify, flash, redirect
import crud


### VIEW ###
# routing request (Telling Flask which URL should correspond with which function)
@app.route('/')
def homepage():
  """Display character names."""

  characters = crud.get_characters()
  # character = crud.get_charID_by_name(characters.id)

  return render_template('index.html', characters=characters)

@app.route('/search', methods=['GET'])
def search():
  """Search for character."""

  search_term = request.args.get('name')
  results = crud.search_character_by_name(search_term)

  if len(results) > 0:
    print('adam strange')
    print('*'*400)
    return redirect(f'/search-results?name={search_term}')
  else:
    flash("No results found")
    return redirect('/')

  return jsonify(results)

@app.route(f'/search-results?name={character.name}')
def return_search():
  "Return search results."



  return render_template('search-results.html', results=results)


# Route "decorator"
@app.route('/<id>')
def characterpage(id=id):
  """View all characters."""

  character = crud.get_char_by_id(id)

  return render_template('character.html', character=character)

@app.route('/react')
def react_test_page():
  """Tests React functionality"""
  return render_template("react_test.html")
