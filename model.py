"""Models for DC Universe Untitled Project."""

from xml.dom.minidom import AttributeList
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# holding off on "nullables" until I can make sure I can get all data needed for db tables


#########################
#######CHARACTERs########
#########################

class Character(db.Model):
  """A character's dossier."""

  __tablename__ = 'characters'

  # char_id = db.Column(db.Integer, primary_key=True)
  char_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  alignment = db.Column(db.String, nullable=False)
  biography = db.Column(db.String)
  earth_name = db.Column(db.Integer) 
  # era_id = db.Column(db.Integer, db.ForeignKey(""))
  gender = db.Column(db.String)
  # media_type = db.Column(db.Integer, db.ForeignKey(""))
  power = db.Column(db.String)  

  # establish relationships, backpopulate
  # media_type = db.relationship('MediaType', backref='characters')
  # era = db.relationship('Era', backref='characters')
  def __repr__(self):
    return f'<Character char_id={self.char_id} name={self.name}>'


#########################
##########ERAS###########
#########################

# class Era(db.Model):
#   """Lists all comic book eras with corresponding dates."""

#   __tablename__ = 'eras'

#   era_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   era_name = db.Column(db.String)
#   era_timeline = db.Column(db.DateTime)

#   # Backref relationship w/Characters table
#   comicEra = db.relationship('ComicEra', back_ref="eras")

#   def __repr__(self):
#     return f'<Era era_id={self.era_id} era_name={self.era_name}>'



#########################
#########MEDIAs##########
#########################

# class Media(db.Model):
#   """All types of media for character appearances, or all types of DC media."""

#   __tablename__ = 'medias'

#   media_type = db.column(db.String, primary_key=True)
#   comic_issue = db.column(db.Integer)
#   film_id = db.column(db.Integer)
#   tv_id = db.column(db.Integer)
#   film_id = db.column(db.Integer)
#   char_id = db.column(db.Integer, db.ForeignKey('characters.char_id'))

#   #Backref relationship w/Characters table

#   # comic = db.Relationship('Comic', back_ref='medias')
#   # film = db.Relationship('Film', back_ref='medias')
#   # tv = db.Relationship('Television', back_ref='medias')
#   comic = db.Relationship('Comic', back_populate='medias')
#   film = db.Relationship('Film', back_populate='medias')
#   tv = db.Relationship('Television', back_populate='medias')

#   def __repr__(self):
#     return f'<Media media_type={self.media_type}>'


# #########################
# #########COMICs##########
# #########################

# class Comic(db.Model):
#   """List of DC comics, or display specific Character's appearance.."""

#   __tablename__ = 'comics'

#   comic_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   comic_issue = db.Column(db.Integer)
#   comic_title = db.Column(db.String)
#   artist = db.Column(db.String)
#   author = db.Column(db.String)
#   comic_overview = db.Column(db.String)
#   comic_type = db.Column(db.String)
#   pub_date = db.Column(db.DateTime)

#   # db.Relationship w/Media table (back_ref)
#   comicEra = db.relationship('ComicEra', back_ref="comics")

#   def __repr__(self):
#     return f'<Comic comic_issue={self.comic_issue} comic_title={self.comic_title}>'


# #########################
# ######COMIC-ERAs#########
# #########################

# class ComicEra(db.Model):
#   "Association table for Comics and Eras."

#   __tablename__ = 'comicEras'

#   comEra_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   comic_issue = db.Column(db.Integer)
#   era_id = db.Column(db.Integer)

#   #Back ref relationship w/comics table
#   #Back ref relationship w/eras table

#   def __repr__(self):
#     return f'<Comic Era comEra_id={self.comEra_id} comic_issue={self.comic_issue} era_id={self.era_id}>'

# #########################
# ##########FILMs##########
# #########################

# class Film(db.Model):
#   """Lists all DC films, or display specific Character's appearance."""

#   __tablename__ = 'films'

#   film_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   film_title = db.Column(db.String)
#   director = db.Column(db.String)
#   media_medium = db.Column(db.String)
#   overview = db.Column(db.String)
#   release_date = db.Column(db.DateTime)
#   actor_s = db.Column(db.String)

#   #db.Relationship w/Media table. (back_ref)

#   def __repr__(self):
#     return f'<Film film_id={self.film_id} film_title={self.film_title}>'
  

# #########################
# #######TELEVISIONs########
# #########################

# class Television(db.Model):
#   """List of all DC television shows, or display a specific Character's appearance."""

#   __tablename__ = 'tv_shows'

#   tv_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#   tv_title = db.Column(db.String)
#   air_date = db.Column(db.DateTime)
#   media_medium = db.Column(db.String)
#   showrunner = db.Column(db.String)
#   tv_overview = db.Column(db.String)

#   #db.Relationship w/Media table (back_ref)

#   def __repr__(self):
#     return f'<Television tv_id={self.tv_id} tv_title={self.tv_title}>'


def connect_to_db(flask_app, db_uri="postgresql:///characters", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
  from server import app

  connect_to_db(app)

