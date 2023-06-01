from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

print(app.config)

# for alchemy to connect; needs to know what to connect (username) and what it is using to connect (ORM) then login then server then database?
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello' 
# has to be exact for it to work  app.config('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app) # create new instance of SQLAlchemy with a connection to the app

# alchemy allows us to put a model on a database
class Card(db.Model): # inheriting from database SQLalchemy structure
    __tablename__ = 'cards' # declare name of table

    id = db.Column(db.Integer, primary_key=True) # tells it is the primary key and it integer
    title = db.Column(db.String(100))
    description = db.Column(db.String())
    date_created = db.Column(db.Date())


# just as per sql tables we dropped first we also need to drop the tables whenever created so it becomes a new slate

@app.cli.command('create') # creates CLI customer commands, string can be anything
def create_db():
    db.drop_all() # drops tables for new slate
    db.create_all() # creates the databases that are defined above (as intepreted language)
    print('Tables created successfull')

@app.cli.command('seed') # creates instance of the Card model in memory
def seed_db():
    # created new instance of Card
    card = Card(
        title = 'Start the project',
        description = 'Stage 1 - Create an ERD',
        date_created = date.today()
    )

    # truncate the Card table same as drop table but only deletes records in table as reseeding
    db.session.query(Card).delete()

    # add card to session (transaction)
    db.session.add(card)

    # commit transaction to database 
    db.session.commit()
    print('Models seeded')

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)