from datetime import datetime
from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=True)
    password_hash = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}'

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    image = db.Column(db.String(128), nullable=True)

    def __repr__(self):
        return f'<City {self.name}'

class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=True)
    description = db.Column(db.Text(), nullable=True)
    image = db.Column(db.String(128), nullable=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=True)

    city = db.relationship('City', backref=db.backref('places', lazy=True))

    def __repr__(self):
        return f'<Place {self.name}'