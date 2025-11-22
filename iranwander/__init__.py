from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

# make database
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_name=Config):
    # static files are two step upper than current dir
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), 'static')
    )
    app.config.from_object(config_name)

    app.config['SECRET_KEY'] = "abc123456789!"
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models
    from .routes.main import main as main_bp
    from .routes.city import city as city_bp
    from .routes.auth import auth as auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(auth_bp)

    return app

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))