from flask import Flask
from os import environ
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.cards_bp import cards_bp
from marshmallow.exceptions import ValidationError

# instead of load dot env wrap in a function
def setup(): # factory function creates and configures object and returns object

    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')   # Can be anything as a secret key, used to sign, verify and create tokens
    # protocol+data base adaptor://user:password@hostname:port/database
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
    # has to be exact for it to work  app.config('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error':f'str{err}'}, 401

    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error':err.__dict__['messages']}, 400

    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(cards_bp)

    return app