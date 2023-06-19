from init import db, ma
from marshmallow import fields, validates, validates_schema
from marshmallow.validate import Length, OneOf, And, Regexp
from marshmallow.exceptions import ValidationError

VALID_STATUSES = ['To Do', 'Done', 'In Progress', 'Testing', 'Deployed'] # constant = variable to not be changed is CAPS

# alchemy allows us to put a model on a database
class Card(db.Model): # inheriting from database SQLalchemy structure
    __tablename__ = 'cards' # declare name of table

    id = db.Column(db.Integer, primary_key=True) # tells it is the primary key and it integer
    
    title = db.Column(db.String(100))
    description = db.Column(db.String())
    status = db.Column(db.String(30))
    date_created = db.Column(db.Date())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    # db.ForeignKey refers to table.column and it already knows cause it exists in the SQLac database 
    user = db.relationship('User', back_populates='cards')  # back_populates = what is the mirror object (connecting point)
    # in both models ONLY if we want it to go both ways
    comments = db.relationship('Comment', back_populates='card', cascade='all, delete')

class CardSchema(ma.Schema): # name convention = modelNameSchema
    # since user is nested it does not know what Schema to serialise with 
    user = fields.Nested('UserSchema', exclude=['password', 'cards', 'comments']) # Tells code user = nested version of UserSchema
    # does not need to list fields list as only one in the link
    comments = fields.List(fields.Nested('CommentSchema', exclude=['user', 'id']))
    title = fields.String(required=True, validate=And(
        Length(min=3, error='Title must be at least 3 characters long'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed') 
        # [] allowable characters + means any number of chars ^$ shows string end and start
        )) # title must be a string and required
    description = fields.String(load_default='') # default if nothing is there as schema is looking for keys when creating cards even if null is not forced
    status = fields.String(load_default=VALID_STATUSES[0]) 
    # status = fields.String(load_default=VALID_STATUSES[0], validate=OneOf(VALID_STATUSES)) # if in the list it is valid

    @validates_schema()
    def validate_status(self, data, **kwargs):
        status = [x for x in VALID_STATUSES if x.upper() == data['status'].upper()]
        if len(status) == 0:
            raise ValidationError(f'Status must be one of: {VALID_STATUSES}')

        data['status'] = status[0]


    class Meta:
        # list model fields wanting to be included
        fields = ('id', 'title', 'description', 'status', 'date_created', 'user')



        