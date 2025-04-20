from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), default='unknown')
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    prediction_score = db.Column(db.Float, nullable=False)
    prediction_result = db.Column(db.String(100), nullable=False)

def init_db(app):
    with app.app_context():
        db.create_all()
