from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from backend.src.main.models.models import db


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///registers.sql"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    migrate = Migrate(app, db)

    return app
