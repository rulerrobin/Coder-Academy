from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

print(app.config)

# for alchemy to connect; needs to know what to connect (username) and what it is using to connect (ORM) then login then server then database?
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello' 
# has to be exact for it to work  app.config('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app) # create new instance of SQLAlchemy with a connection to the app

# alchemy allows us to put a model on a database
class Card(db.Model): # inheriting from database SQLalchemy structure
    id = db.Column(db.Integer, primary_key=True) # tells it is the primary key and it integer
    title = db.Column(db.String(100))
    description = db.Column(db.String())
    date_created = db.Column(db.Date())



@app.cli.command('create') # creates CLI customer commands, string can be anything
def create_db():
    db.create_all() # creates the databases that are defined above (as intepreted language)
    print('Tables created successfull')

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)