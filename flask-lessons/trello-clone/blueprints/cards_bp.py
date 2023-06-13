from flask import Blueprint, request, abort
from models.card import Card, CardSchema
from init import db
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required
from datetime import date

cards_bp = Blueprint('card', __name__, url_prefix='/cards')

@cards_bp.route('/')
@jwt_required() # protects to say token is needed
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


# Get one card
@cards_bp.route('/<int:card_id>')
@jwt_required()
def one_card(card_id):
    stmt = db.select(Card).filter_by(id=card_id)
    card = db.session.scalar(stmt)
    if card:
        return CardSchema().dump(card)
    else: 
        return {'error':'Card not found'}, 404
    

# Create a new card
@cards_bp.route('/', methods=['POST']) 
@jwt_required()
# create is always same as get all route it's different because of verb therefore it is interpreted differently from the other
def create_card():
    # Load incoming POST data via the schema
    card_info = CardSchema().load(request.json)
    # Create a new card instance from the card_info
    card = Card(
        title = card_info['title'],
        description = card_info['description'],
        status = card_info['status'],
        date_created = date.today()
    )
    # Add and commit new card to session
    db.session.add(card)
    db.session.commit()
    # Send new card back to client
    print(card_info)
    return CardSchema().dump(card),201

# Update a card
@cards_bp.route('/<int:card_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_card(card_id):
    admin_required()    
    stmt = db.select(Card).filter_by(id=card_id)
    card = db.session.scalar(stmt)
    card_info = CardSchema().load(request.json)

    if card: 
# . description because card is instance of model because it is a class, columns are attributes like any other class
# card info is dictionary so square is keys to access 
        card.title = card_info.get('title', card.title) # get value of key title and if doesnt exist use the second parameter
        card.description = card_info['description'],
        card.status = card_info['status'],
        date_created = date.today()   
        db.session.commit() # no add as just aditing existing
        return CardSchema().dump(card)     
    else: 
        return {'error':'Card not found'}, 404
    
@cards_bp.route('/<int:card_id>', methods=['DELETE'])
@jwt_required()
def delete_card(card_id):
    admin_required()    
    stmt = db.select(Card).filter_by(id=card_id)
    card = db.session.scalar(stmt)
    if card:
        db.session.delete(card)
        db.session.commit()
        return{}, 200
    else: 
        return {'error':'Card not found'}, 404