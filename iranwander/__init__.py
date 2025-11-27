from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
import os
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()


def create_app(config_name=Config):
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), 'static')
    )

    app.config.from_object(config_name)

    app.config['SECRET_KEY'] = "abc123456789!"

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "لطفاً ابتدا وارد شوید."
    login_manager.login_message_category = "info"

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'talebimahdyar8@gmail.com'
    app.config['MAIL_PASSWORD'] = 'ejrf qrac yaun dzsd'  
    app.config['MAIL_DEFAULT_SENDER'] = 'talebimahdyar8@gmail.com'

    app.mail = mail

    from . import models

    from .routes.main import main as main_bp
    from .routes.city import city as city_bp
    from .routes.auth import auth as auth_bp
    from .routes.api import api as api_bp
    from .routes.user import user_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(user_bp)

    return app

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))