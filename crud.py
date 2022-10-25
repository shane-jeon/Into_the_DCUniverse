"""CRUD Operations."""

from model import db, Character, connect_to_db

def create_char(char_id, name, alignment):
  """Create and return a new character."""
  char = Character(char_id=char_id,
                   name=name,
                   alignment=alignment
  )

  db.session.add(char)
  db.session.commit()

  return char

def return_all():
  """Return all characters."""

  return Character.query.all()

def get_char_by_id(char_id):
  """Gets character by char_id."""

  char = Character.query.get(char_id)

  return char

# IDs appear to be not consecutive...create a function to get IDs by name... 


if __name__ == '__main__':
  from server import app
  connect_to_db(app)