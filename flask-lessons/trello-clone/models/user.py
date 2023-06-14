from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    cards = db.relationship('Card', back_populates='user') # relate to Card model in database

class UserSchema(ma.Schema):
    #
    cards = fields.List(fields.Nested('CardSchema', exclude=['user', 'id'])) # nested list of schemas because its many cards to one user (cards = plural)
    # exclude user as it's nested looped creating an infinite loop
    comments = fields.Nested('CommentSchema', exclude=['user', 'id'])

    class Meta:
        fields = ('name', 'email', 'password', 'is_admin','cards') # Only these fields to show 