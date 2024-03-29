from flask import Blueprint
from flask import Flask, request, abort
from datetime import timedelta
from models.user import User, UserSchema
from init import db, bcrypt
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/users')
def all_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many=True, exclude=['password']).dump(users)

@auth_bp.route('/register', methods=['POST']) # second parameter can put list of methods can use
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
 
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        stmt = db.select(User).filter_by(email=request.json['email']) # filter by can do equality, less flexible than a .where(user.email==request)
        user = db.session.scalar(stmt) 
        
        if user and bcrypt.check_password_hash(user.password, request.json['password']): # checks user is true otherwise skips
            token = create_access_token(identity=user.id, expires_delta=timedelta(days=1)) # expiry of token
            return {'token': token, 'user': UserSchema(exclude=['password', 'cards', 'comments']).dump(user)}
        else:
            return {'error': 'Invalid email address or password'}, 401
    except KeyError:
        return {'error': 'Email and password are required'}, 400





def admin_or_owner_required(owner_id):
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and (user.is_admin or user_id == owner_id)):
        abort(401, description="You must be an admin or the owner")

