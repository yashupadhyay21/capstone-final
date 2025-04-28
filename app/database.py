# database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), default='unknown')
    email = db.Column(db.String(100), unique=True, nullable=False)  # Ensure email is unique and required
    password = db.Column(db.String(150), nullable=False)  # Password cannot be null
    prediction_score = db.Column(db.Float, nullable=False)
    prediction_result = db.Column(db.String(100), nullable=False)

def init_db(app):
    with app.app_context():
        db.create_all()
