"""CRUD Operations."""

from model import db, Character, connect_to_db

def create_character(id, image, name, real_name, alias, gender, species, biography, power, friend, enemy, team, first_appearance, appearance_count, issue_credit, creator):
  """Create and return a new character."""
  char = Character(
                   id=id,
                   image=image,
                   name=name,
                   real_name=real_name,
                   alias=alias
                   gender=gender,
                   species=species,
                  #  alignment=alignment,
                   biography=biography,
                   power=power,
                   friend=friend,
                   enemy=enemy, 
                   team=team,
                   first_appearance=first_appearance,
                   appearance_count=appearance_count,
                   issue_credit=issue_credit,
                   creator=creator
  )

  # db.session used for database transactions (nothing to do with Flask 'session')
  # db.session stores modifications made to database

  # to add new object
  db.session.add(char)
  # database will not actually be modified unless following call included
  db.session.commit()

  return char

def get_char_by_id(char_id):
  """Gets character by char_id."""

  char = Character.query.get(char_id)

  return char

# # IDs appear to be not consecutive...create a function to get IDs by name... //RESOLVED 10/25/2022

def get_charID_by_name(name):

  return Character.query.filter_by(name=name)

def get_characters():
  """Return all characters."""

  return Character.query.all()

if __name__ == '__main__':
  from server import app
  connect_to_db(app)