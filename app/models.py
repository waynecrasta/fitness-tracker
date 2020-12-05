from sqlalchemy import func

from app import db


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=1)
    type = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    time_created = db.Column(db.DateTime, server_default=func.now())
