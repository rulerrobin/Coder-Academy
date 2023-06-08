from flask import Flask, request, abort
from datetime import date
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity 
from datetime import timedelta
from os import environ
from dotenv import load_dotenv
from models.user import User, UserSchema
from models.card import Card, CardSchema
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import db_commands


load_dotenv()

print(environ)

app = Flask(__name__)

db.init_app(app)
ma.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)

# protocol+data base adaptor://user:password@hostname:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
# has to be exact for it to work  app.config('SQLALCHEMY_DATABASE_URI')
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')  # Can be anything as a secret key, used to sign, verify and create tokens



def admin_required():
    user_email = get_jwt_identity()
    stmt = db.select(User).filter_by(email=user_email)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401)

@app.errorhandler(401)
def unauthorized(err):
    return {'error':'You must be an admin'}, 401

app.register_blueprint(db_commands)

@app.route('/register', methods=['POST']) # second parameter can put list of methods can use
def register():
    try:
        # Parse, sanitize and validate the incoming JSON data
        # via the schema. 
        user_info = UserSchema().load(request.json) 
        # Create a new User model instance with the scheme data from the incoming JSON request
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

        # return the new user excluding password
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409

@app.route('/login', methods=['POST'])
def login():
    try:
        stmt = db.select(User).filter_by(email=request.json['email']) # filter by can do equality, less flexible than a .where(user.email==request)
        user = db.session.scalar(stmt) 
        
        if user and bcrypt.check_password_hash(user.password, request.json['password']): # checks user is true otherwise skips
            token = create_access_token(identity=user.email, expires_delta=timedelta(days=1)) # expiry of token
            return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
        else:
            return {'error': 'Invalid email address or password'}, 401
    except KeyError:
        return {'error': 'Email and password are required'}, 400


@app.route('/cards')
@jwt_required() # protects to say token is needed
def all_cards():
    admin_required()
    
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