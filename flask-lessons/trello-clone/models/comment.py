from init import db, ma
from marshmallow import fields

# alchemy allows us to put a model on a database
class Comment(db.Model): # inheriting from database SQLalchemy structure
    __tablename__ = 'comments' # declare name of table

    id = db.Column(db.Integer, primary_key=True) # tells it is the primary key and it integer
    
    message = db.Column(db.String())
    date_created = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # db.ForeignKey refers to table.column and it already knows cause it exists in the SQLac database 
    user = db.relationship('User', back_populates='comments')  # back_populates = what is the mirror object (connecting point)
    # in both models ONLY if we want it to go both ways

    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
    card = db.relationship('Card', back_populates='comments')

class CommentSchema(ma.Schema): # name convention = modelNameSchema
    # since user is nested it does not know what Schema to serialise with 
    user = fields.Nested('UserSchema', only=['name', 'email', 'is_admin']) # Tells code user = nested version of UserSchema
    card = fields.Nested('CardSchema', only=['title', 'description', 'status'])
    # does not need to list fields list as only one in the link
    class Meta:
        # list model fields wanting to be included
        fields = ('id', 'message', 'date_created', 'card', 'user')



        