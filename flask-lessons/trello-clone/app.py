from flask import Flask
from os import environ
from dotenv import load_dotenv
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.cards_bp import cards_bp

load_dotenv()

print(environ.get('DB_URI'))

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
    return {'error':'You must be an admin'}, 401

app.register_blueprint(cli_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(cards_bp)




if __name__ == '__main__':
    app.run(debug=True)