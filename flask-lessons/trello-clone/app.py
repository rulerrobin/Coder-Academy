from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

print(app.config)


# for alchemy to connect; needs to know what to connect (username) and what it is using to connect (ORM) then login then server then database?

# protocol+data base adaptor://user:password@hostname:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello' 
# has to be exact for it to work  app.config('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app) # create new instance of SQLAlchemy with a connection to the app
ma = Marshmallow(app)
bcrypt = Bcrypt(app) 

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email', 'password', 'is_admin') # Only these fields to show 

# alchemy allows us to put a model on a database
class Card(db.Model): # inheriting from database SQLalchemy structure
    __tablename__ = 'cards' # declare name of table

    id = db.Column(db.Integer, primary_key=True) # tells it is the primary key and it integer
    title = db.Column(db.String(100))
    description = db.Column(db.String())
    status = db.Column(db.String(30))
    date_created = db.Column(db.Date())

class CardSchema(ma.Schema): # name convention = modelNameSchema
    class Meta:
        # list model fields wanting to be included
        fields = ('id', 'title', 'description', 'status', 'date_created')
        


# just as per sql tables we dropped first we also need to drop the tables whenever created so it becomes a new slate

@app.cli.command('create') # creates CLI customer commands, string can be anything
def create_db():
    db.drop_all() # drops tables for new slate
    db.create_all() # creates the databases that are defined above (as intepreted language)
    print('Tables created successfull')

@app.cli.command('seed') # creates instance of the Card model in memory
def seed_db():

    users = [
        User(
            email = 'admin@spam.com',
            password = bcrypt.generate_password_hash('spinynorman').decode('utf-8'),# decode utf converts to show as base 64
            is_admin = True
        ),
        User(
            name = 'John Cleese',
            email = 'cleese@spam.com', 
            password = bcrypt.generate_password_hash('tisbutascratch').decode('utf-8'),
        )
    ]

    # created new instance of Card
    cards = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create an ERD',
            status = "Done",
            date_created = date.today()
        ),

        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement several queries',
            status = "In Progress",
            date_created = date.today()
        ),

        Card(
            title = 'Marshmallow',
            description = 'Stage 3 - Implement jsonify of models',
            status = "In Progress",
            date_created = date.today()
        )
    ]

    # truncate the Card table same as drop table but only deletes records in table as reseeding
    db.session.query(Card).delete()
    db.session.query(User).delete()

    # add card to session (transaction)
    db.session.add_all(cards)
    db.session.add_all(users)


    # commit all transactions to database 
    db.session.commit()
    print('Models seeded')

@app.route('/register', methods=['POST']) # second parameter can put list of methods can use
def register():
    try:
        # Parse, sanitize and validate the incoming JSON data
        # via the schema. 
        user_info = UserSchema().load(request.json) 
        # Create a new User model instance with the scheme data 
        user = User(
            email = user_info['email'],
            password = bcrypt.generate_password_hash(user_info['password']).decode('utf-8'),
            name = user_info['name']
        )

        # add and commit the new user
        db.session.add(user)
        db.session.commit()

        # print(request.json) # request function prints information about incoming request # .json as incoming json object allows to see as python object
        # print (user.__dict__)

        # return the new user
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409

@app.route('/cards')
def all_cards():
    # GOAL - select * from cards;
    stmt = db.select(Card).order_by(Card.status.desc())
    # .limit(2) # do a select query from cards limited to 2 # if only 1 its returned as an item/object

    # executes statement above
    # cards = db.session.execute(stmt)  # default tuple
    cards = db.session.scalars(stmt).all() # scalars uses a list
    # returns model instances # all will always return a list
    return CardSchema(many=True).dump(cards) # default is one so need many = True for more than one
    # dump vs dumps = dump changes to python which allows marshmallow to understand
    # pass object that needs to be jsonified # have to set many=True otherwise default it will expect only one to be returned otherwise it will be ignored
    # cards = db.session.scalars(stmt).first() # returns first one

    # print(cards) 

    # for card in cards: # loops over 
    #     print(card.__dict__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)