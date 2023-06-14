from init import db, ma
from marshmallow import fields

# alchemy allows us to put a model on a database
class Card(db.Model): # inheriting from database SQLalchemy structure
    __tablename__ = 'cards' # declare name of table

    id = db.Column(db.Integer, primary_key=True) # tells it is the primary key and it integer
    
    title = db.Column(db.String(100))
    description = db.Column(db.String())
    status = db.Column(db.String(30))
    date_created = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # db.ForeignKey refers to table.column and it already knows cause it exists in the SQLac database 

    user = db.relationship('User', back_populates='cards')  # back_populates = what is the mirror object (connecting point)
    # in both models ONLY if we want it to go both ways
    comments = db.relationship('Comment', back_populates='card')

class CardSchema(ma.Schema): # name convention = modelNameSchema
    # since user is nested it does not know what Schema to serialise with 
    user = fields.Nested('UserSchema', exclude=['password', 'cards']) # Tells code user = nested version of UserSchema
    # does not need to list fields list as only one in the link
    comments = fields.List(fields.Nested('CommentSchema', exclude=['user', 'id']))

    class Meta:
        # list model fields wanting to be included
        fields = ('id', 'title', 'description', 'status', 'date_created', 'user')



        