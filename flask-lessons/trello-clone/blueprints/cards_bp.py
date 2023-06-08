from flask import Blueprint
from models.card import Card, CardSchema
from init import db
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

cards_bp = Blueprint('card', __name__)

@cards_bp.route('/cards')
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