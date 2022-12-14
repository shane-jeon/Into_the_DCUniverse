"""CRUD Operations."""

from model import db, Character, connect_to_db

def create_character(id, image, name, real_name, alias, gender, origin, biography, power, friend, enemy, team, first_appearance, appearance_count, comic_issue, creator):
  """Create and return a new character."""
  char = Character(
                   id=id,
                   image=image,
                   name=name,
                   real_name=real_name,
                   alias=alias,
                   gender=gender,
                   origin=origin,
                  #  alignment=alignment,
                   biography=biography,
                   power=power,
                   friend=friend,
                   enemy=enemy, 
                   team=team,
                   first_appearance=first_appearance,
                   appearance_count=appearance_count,
                   comic_issue=comic_issue,
                   creator=creator
  )

  # db.session used for database transactions (nothing to do with Flask 'session')
  # db.session stores modifications made to database

  # to add new object
  db.session.add(char)
  print('*'*500, 'HERE')
  print(char)
  # database will not actually be modified unless following call included
  db.session.commit()
  print('*'*500, 'COMMIT COMPLETE')

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
  from app import app
  connect_to_db(app)