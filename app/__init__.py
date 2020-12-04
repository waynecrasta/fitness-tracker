from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.views import mod_auth as auth_mod
app.register_blueprint(auth_mod)


