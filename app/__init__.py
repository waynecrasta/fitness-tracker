from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config["SECRET_KEY"] = config.SECRET_KEY
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.views import main

app.register_blueprint(main)
