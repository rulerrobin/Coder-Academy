from flask import Flask, jsonify

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

## DB CONNECTION AREA

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://tomato:<password>@localhost:5432/ripe_tomatoes_db'
# config = protocol+adaptor for db ://user:password@hostname:port/database

db = SQLAlchemy(app)
ma = Marshmallow(app)

# CLI COMMANDS AREA

@app.cli.command('create') # Drop previous table for new slate and make table
def create_db():
  db.drop_all()
  db.create_all()
  print('Created')

@app.cli.command('seed') # Seeds the tables
def seed_db():

  actors = [

    Actor(
      first_name = 'Tom',
      last_name = 'Holland',
      gender = 'male',
      country = 'UK'
    ),
    Actor(
      first_name = 'Marisa',
      last_name = 'Tomei',
      gender = 'female',
      country = 'USA'
    ),

    Actor(
      first_name = 'Henry',
      last_name = 'Cavill',
      gender = 'male',
      country = 'UK'
    ),
    Actor(
      first_name = 'Matthew',
      last_name = 'Mercer',
      gender = 'male',
      country = 'USA'
    )
  ]

  movies = [
    Movie(
      genre = 'Action',
      length = 148,
      title = 'Spider-Man: No Way Home',
      year = 2021
    ),

    Movie(
      genre = 'Sci-Fi',
      length = 155,
      title = 'Dune',
      year = 2021
    )
  ]

  # truncate table as if it has cascade delete if exists
  db.session.query(Actor).delete() 
  db.session.query(Movie).delete()

  # add card to session (transaction)
  db.session.add_all(actors)
  db.session.add_all(movies)

  # commit the change
  db.session.commit()
  print ('Models seeded')

# MODELS AREA

class Actor(db.Model):
  __tablename__ = 'actors'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String)
  last_name = db.Column(db.String)
  gender = db.Column(db.String)
  country = db.Column(db.String)

class Movie(db.Model):
  __tablename__  = 'movies'

  id = db.Column(db.Integer, primary_key=True)
  genre = db.Column(db.String)
  length = db.Column(db.Integer)
  title = db.Column(db.String)
  year = db.Column(db.Integer)


# SCHEMAS AREA

class ActorSchema(ma.Schema):
  class Meta:
    fields = ('id', 'first_name', 'last_name', 'gender', 'country')

class MovieSchema(ma.Schema):
  class Meta:
    fields = ('id', 'genre', 'length', 'title', 'year')

# ROUTING AREA

@app.route("/")
def hello():
  return "Welcome to Ripe Tomatoes API"

@app.route("/actors")
def all_actors():
    stmt = db.select(Actor)
    actors = db.session.scalars(stmt).all()
    serialized_actors = ActorSchema(many=True).dump(actors)
    return jsonify(serialized_actors)

@app.route("/movies")
def all_movies():
  stmt = db.select(Movie)
  movies = db.session.scalars(stmt).all()
  serialized_movies = MovieSchema(many=True).dump(movies)
  return jsonify(serialized_movies)

if __name__ == '__main__':
  app.run(debug=True)