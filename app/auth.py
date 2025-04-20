from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from .database import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    # Check if user already exists by email
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'message': 'User already exists'}), 409
    
    # Hash the password before storing
    hashed_pw = generate_password_hash(data['password'])
    
    # Create a new user instance with email, username, and hashed password
    new_user = User(email=data['email'], username=data['username'], password=hashed_pw)
    
    # Add the user to the database and commit the changes
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    # Retrieve user by email
    user = User.query.filter_by(email=data['email']).first()
    
    # Check if the user exists and the password matches
    if user and check_password_hash(user.password, data['password']):
        return jsonify({'message': 'Login successful'}), 200
    
    # If credentials are invalid, return an error
    return jsonify({'message': 'Invalid credentials'}), 401
