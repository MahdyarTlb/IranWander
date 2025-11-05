from flask import Flask
from flask_migrate import Migrate
from .extensions import db, login_manager
from config import Config
from .models import User
import os

migrate = Migrate()

def create_app(config_name=Config):
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), 'static')
    )
    app.config.from_object(config_name)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from . import models
    from .routes.main import main as main_bp
    from .routes.city import city as city_bp
    from .routes.place import place as place_bp
    from .routes.admin import admin as admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(city_bp)
    app.register_blueprint(place_bp)
    app.register_blueprint(admin_bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))