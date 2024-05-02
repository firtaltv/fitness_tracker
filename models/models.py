from app import db
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    age = db.Column(db.Integer)

    # activities = db.relationship("Activity", backref="users")

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'weight': self.weight,
            'height': self.height,
            'age': self.age
        }

    def get_weight_score(self):
        ideal_body_weight = 22 * ((self.height/100)**2)
        if self.weight < ideal_body_weight - 6:
            return {'message': f'You should gain some weight, your ideal weight is {ideal_body_weight} ± 5 kgs'}
        if self.weight > ideal_body_weight + 6:
            return {'message': f"If you're not muscular, consider losing some weight, your ideal is {ideal_body_weight} kgs"}
        if abs(self.weight - ideal_body_weight) <= 6:
            return {'message': 'Your weight is ideal. Looking good!'}


class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    activity_time = db.Column(db.Integer, nullable=False)  # Assuming this represents time in minutes
    datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @staticmethod
    def count_calories(activity, duration):
        calorie_formulas = {
            'Running': 704,
            'Walking': 320,
            'Swimming1': 423,
            'Swimming2': 704,
            'Light Workout': 204,
            'Intensive Workout': 633
        }
        calories = (duration / 60) * calorie_formulas.get(activity)
        return calories

    @classmethod
    def get_all(cls, id):
        return cls.query.filter(cls.user_id==id).all()


class ActivityHistory(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), primary_key=True)
