from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy() # create new instance of SQLAlchemy with a connection to the app
ma = Marshmallow()
bcrypt = Bcrypt() 
jwt = JWTManager()