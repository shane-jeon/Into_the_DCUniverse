"""MOdels for DC Universe Untitled Project."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
  """A character."""

  __tablename__ = 'characters'

  char_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
  char_name = db.Column(db.String)
  biography = db.Column(db.varChar)
  gender = db.Column(db.String)
  archetype = db.Column(db.String)
  power = db.Column(db.String)
  media_type = db.Column(db.Integer, db.ForeignKey(""))
  earth_name = db.Column(db.Integer, db.ForeignKey("")) 

  def __repr__(self):
    return f'<Character char_id={self.char_id} char_name={self.char_name}>'

class Media(db.Model):
  """All types of character media appearances."""

  __tablename__ = 'media'

  media_type = db.column()