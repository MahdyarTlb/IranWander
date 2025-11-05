from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os

# make database
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=Config):
    # static files are two step upper than current dir
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
        static_folder=os.path.join(os.path.dirname(__file__), 'static')
    )
    app.config.from_object(config_name)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models
    from .routes.main import main as main_bp
    from .routes.city import city as city_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(city_bp)

    return app