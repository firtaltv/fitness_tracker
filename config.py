import os


class MainConfig:
    DEBUG = True
    TESTING = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")
