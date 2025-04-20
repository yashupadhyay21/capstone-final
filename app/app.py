from flask import Flask, render_template
from .auth import auth_bp  # Import the auth blueprint
from .predict import predict_bp  # Import the predict blueprint
from .database import db, init_db  # Import db and init_db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super-secret-key'  # Secret key for sessions

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)  # Initialize SQLAlchemy
    init_db(app)  # Create tables if not present

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(predict_bp, url_prefix='/predict')

    # ✅ Serve index.html at root
    @app.route('/')
    def home():
        return render_template('index.html')

    return app

# Create and run the Flask app
app = create_app()

if __name__ == '__main__':
    # Print registered routes
    with app.app_context():
        print("Registered Routes:")
        for rule in app.url_map.iter_rules():
            print(rule)

    app.run(debug=True)
