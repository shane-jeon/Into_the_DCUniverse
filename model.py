"""Models for DC Universe Untitled Project."""

# from xml.dom.minidom import AttributeList
from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# db object gives access to db.Model class to define models and db.session to execute queries

db = SQLAlchemy()

#########################
########CHARACTER########
#########################

# subclass 'db.Model' defines model class
class Character(db.Model):
  """A character profile."""
  __tablename__ = 'character'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  image = db.Column(db.String)
  name = db.Column(db.String(50), nullable=False)
  # alignment = db.Column(db.String(15), nullable=False)
  gender = db.Column(db.String(15), nullable=False)
  # species = db.Column(db.String)
  biography = db.Column(db.String, nullable=False)
  # earth_id = db.Column(db.String, db.ForeignKey('earth.id')) 
  # era_id = db.Column(db.Integer, db.ForeignKey('era.id'))
  # media_id = db.Column(db.Integer, db.ForeignKey('media.id'))
  power = db.Column(db.String)
  creator = db.Column(db.String)  
  # first_appearance = db.Column(db.String)

  # relationship w/media_association table

  def __repr__(self):
    return f'''
    
    <CharacterID={self.id} ,
    name={self.name} ,
    biography={self.biography} ,
    img={self.image}>
    '''


# #########################
# ##########MEDIA##########
# #########################

# # class Media(db.Model):
# #   """Association table to access comics, film, and television."""

# #   __tablename__ = 'media'

# #   id = db.column(db.String, primary_key=True)
# #   comic_id = db.column(db.Integer, db.ForeignKey('comic.id'))
# #   film_id = db.column(db.Integer, db.ForeignKey('film.id'))
# #   tv_id = db.column(db.Integer, db.ForeignKey('television.id'))
# #   char_id = db.column(db.Integer, db.ForeignKey('character.id'))

# media_association= db.Table('media_association',
#   # db.Model.metadata,
#   db.Column('char_id', db.ForeignKey('character.id'), primary_key=True),
#   db.Column('comic_id', db.ForeignKey('comic.id'), primary_key=True),
#   db.Column('film_id', db.ForeignKey('film.id'), primary_key=True),
#   db.Column('tv_id', db.ForeignKey('television.id'), primary_key=True)

#   # Relationships with:
#       # character Model
#       # comic Model
#       # film Model
#       # television Model
# )

# #########################
# ##########EARTH##########
# #########################

# class Earth(db.Model):
#   """List of DC comics."""

#   __tablename__ = 'earth'

#   id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   earth_name = db.Column(db.String)
#   deceased_chars = db.Column(db.String)
#   char_id = db.Column(db.Integer, db.ForeignKey('character.id'))
#   comic_id = db.Column(db.Integer, db.ForeignKey('comic.id'))
#   film_id = db.Column(db.Integer, db.ForeignKey('film.id'))
#   tv_id = db.Column(db.Integer, db.ForeignKey('television.id'))

#   # relationship to character, comic, film, and tv Model

#   def __repr__(self):
#     return f'<Earth id={self.id} earth_name={self.earth_name}>'

# #########################
# #########COMIC###########
# #########################

# class Comic(db.Model):
#   """List of DC comics."""

#   __tablename__ = 'comic'

#   id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   comic_issue = db.Column(db.Integer)
#   comic_title = db.Column(db.String)
#   author = db.Column(db.String)
#   artist = db.Column(db.String)
#   overview = db.Column(db.String)
#   comic_type = db.Column(db.String)
#   pub_date = db.Column(db.DateTime)
#   # era is either pre, mid, post crisis
#   era = db.Column(db.String)
#   # age is what has it's own table
#   age_id = db.Column(db.Integer, db.ForeignKey('age.id'))

#   # relationship w/media table

#   def __repr__(self):
#     return f'<Comic id={self.id} comic_issue={self.comic_issue} comic_title={self.comic_title}>'

 

# #########################
# ##########AGE############
# #########################

# class Age(db.Model):
#   """Lists all comic book ages with corresponding dates."""

#   __tablename__ = 'age'

#   id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   age = db.Column(db.String)
#   time_period = db.Column(db.DateTime)

#   # relationship to comic table


#   def __repr__(self):
#     return f'<age id={self.id} age={self.age}>'



# # #########################
# # ##########FILM###########
# # #########################

# class Film(db.Model):
#   """Lists all DC films."""

#   __tablename__ = 'film'

#   id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   title = db.Column(db.String, nullable=False)
#   summary = db.Column(db.String)
#   director = db.Column(db.String)
#   media_medium = db.Column(db.String)
#   release_date = db.Column(db.DateTime, nullable=False)
#   act_talent = db.Column(db.String)
#   char_id = db.Column(db.Integer, db.ForeignKey('character.id'))

#   #relationship w/media, character table

#   def __repr__(self):
#     return f'<Film id={self.id} film_title={self.title}>'
  

# # #########################
# # #######TELEVISION#########
# # #########################

# class Television(db.Model):
#   """List of all DC television shows."""

#   __tablename__ = 'television'

#   id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   title = db.Column(db.String)
#   air_date = db.Column(db.DateTime)
#   media_medium = db.Column(db.String)
#   showrunner = db.Column(db.String)
#   summary = db.Column(db.String)
#   char_id = db.Column(db.Integer, db.ForeignKey('character.id'))

#   #db.Relationship w/Media, character tables

#   def __repr__(self):
#     return f'<Television id={self.id} title={self.title}>'


def connect_to_db(flask_app, db_uri='postgresql:///characters', echo=True):
  """Connect to database."""

  # Tells SQLAlchemy what database to connect to
  flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
  # Will output raw SQL, executed by SQLAlchemy (so that's why I see the SQL query in the terminal)
  flask_app.config['SQLALCHEMY_ECHO'] = echo
  flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # connects databse with Flask app
  db.app = flask_app
  # call initializes SQLAlchemy extension class with the application
  db.init_app(flask_app)

  print("Connected to DB (model.py)")


if __name__ == "__main__":
  from server import app

  # connection call
  # Any errors about db connection that will arise, check connect_to_db(app) is called before app.run() 
  connect_to_db(app)



# #########################
# ######USER_ACCOUNT#######
# #########################
# class User_Account(db.Model):
#   """A user's account."""
#   __tablename__ = 'user_account'

#   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   username = db.Column(db.String, unique=True, nullable=False)
#   email = db.Column(db.String, unique=True, nullable=False)
#   password = db.Column(db.String, nullable=False)
#   avatar = db.Column(db.String)
#   bookmark_id = db.Column(db.Integer, db.ForeignKey('bookmark.id'))

# #########################
# #####USER_BOOKMARK#######
# #########################
# # association table
# user_bookmark= db.Table('user_bookmark',
#   # db.Model.metadata,
#   db.Column('user_id', db.ForeignKey('user.id'), primary_key=True),
#   db.Column('bookmark_id', db.ForeignKey('bookmark.id'), primary_key=True),

#   # Relationships with:
#       # user Model
#       # bookmark Model
# )

# #########################
# ########BOOKMARK#########
# #########################
# class Bookmark(db.Model):
#   """A user's account."""
#   __tablename__ = 'bookmark'

#   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#   user_id = db.Column(db.Integer, db.ForeignKey('user_account.id'))
#   char_id = db.Column(db.Integer, db.ForeignKey('character.id'))

#   # relationship with User, Character Model
