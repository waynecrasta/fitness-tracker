from flask_login import UserMixin
from sqlalchemy import func

from app import db
from app import login_manager


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    time_created = db.Column(db.DateTime, server_default=func.now())

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=1)
    type = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    time_created = db.Column(db.DateTime, server_default=func.now())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
