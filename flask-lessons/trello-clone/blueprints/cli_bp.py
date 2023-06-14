from flask import Blueprint
from datetime import date
from models.user import User
from models.card import Card
from init import db, bcrypt
from models.comment import Comment


# because these were connected directly to app through @app need to create a type of container as it's separated

cli_bp = Blueprint('db', __name__) # unique name, typically __name__ dunder

# to access commands instead of flask seed it needs to be # `flask db seed`` in reference to the group for blueprints
# just as per sql tables we dropped first we also need to drop the tables whenever created so it becomes a new slate
@cli_bp.cli.command('create') # creates CLI customer commands, string can be anything
def create_db():
    db.drop_all() # drops tables for new slate
    db.create_all() # creates the databases that are defined above (as intepreted language)
    db.session.commit() #
    print('Tables created successfull')

@cli_bp.cli.command('seed') # creates new base data to tables
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

    db.session.query(User).delete()
    db.session.add_all(users)
    db.session.commit()

    print(users[0].id)

    # created new instance of Card
    cards = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create an ERD',
            status = "Done",
            date_created = date.today(),
            user_id=users[0].id
        ),

        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement several queries',
            status = "In Progress",
            date_created = date.today(),
            user_id=users[0].id
        ),

        Card(
            title = 'Marshmallow',
            description = 'Stage 3 - Implement jsonify of models',
            status = "In Progress",
            date_created = date.today(),
            user_id=users[1].id
        )
    ]

    # truncate the Card table same as drop table but only deletes records in table as reseeding
    db.session.query(Card).delete()
    db.session.add_all(cards)  # add card to session (transaction)
    db.session.commit() # commit all transactions to database 

    comments = [
        Comment(
            message='Comment 1',
            date_created=date.today(),
            user_id=users[0].id,
            card_id=cards[1].id
        ),
                Comment(
            message='Comment 2',
            date_created=date.today(),
            user_id=users[1].id,
            card_id=cards[1].id
        ),
                Comment(
            message='Comment 3',
            date_created=date.today(),
            user_id=users[1].id,
            card_id=cards[0].id
        )

    ]

        # truncate the Card table same as drop table but only deletes records in table as reseeding
    db.session.query(Comment).delete()
    db.session.add_all(comments)  # add card to session (transaction)
    db.session.commit() # commit all transactions to database 

    print('Models seeded')