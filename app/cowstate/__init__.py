from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .views import main_views
import config


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    ###### DATABASE ######
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    ###### views #######
    app.register_blueprint(main_views.bp)

    return app