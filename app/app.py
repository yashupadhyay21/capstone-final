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

    db.init_app(app)
    init_db(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(predict_bp, url_prefix='/predict')

    # Home route
    @app.route('/')
    def home():
        return render_template('index.html')

    return app


app = create_app()

if __name__ == '__main__':
    with app.app_context():
        print("Registered Routes:")
        for rule in app.url_map.iter_rules():
            print(rule)

    # ✅ Listen on all interfaces for Docker
    app.run(host='0.0.0.0', port=5000, debug=True)
