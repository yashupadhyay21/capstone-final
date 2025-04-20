# app.py
from flask import Flask, render_template
from flask_login import LoginManager
from .auth import auth_bp
from .predict import predict_bp
from .database import db, init_db, User

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super-secret-key'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    init_db(app)

    # Flask-Login setup
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(predict_bp, url_prefix='/predict')

    @app.route('/')
    def home():
        return render_template('home.html')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
