from init import db, ma

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
        