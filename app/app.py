from flask import Flask
import logging
from app.config import Config
from app.routes import user_bp
from app.db import db, migrate, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Basic logging configuration so module loggers (e.g. app.routes) are visible
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    logging.getLogger().setLevel(logging.INFO)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    app.register_blueprint(user_bp)

    return app
