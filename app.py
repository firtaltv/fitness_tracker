from flask import Flask
import os
from flask_migrate import Migrate
import dotenv
from config import MainConfig
from database import db
from routes.home import home
from routes.auth import auth
from routes.user import user
from routes.activity import activity
from flask_login import LoginManager

dotenv.load_dotenv(".env")

def create_app():
    app = Flask(__name__)
    app.config.from_object(MainConfig)
    print(os.environ)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URL")
    app.register_blueprint(auth)
    app.register_blueprint(home)
    app.register_blueprint(user)
    app.register_blueprint(activity)
    db.init_app(app)

    Migrate(app, db)
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    from models.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    return app
