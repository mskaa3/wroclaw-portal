"""database configuration file"""

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """base config"""

    SECRET_KEY = environ.get("SECRET_KEY")
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MIGRATE_REPO = path.join(basedir, "db_repository")

    OKTA_ORG_URL = "https://dev-73352242.okta.com/"
    OKTA_AUTH_TOKEN = "00wypJxwIxxILACoZp3bnbxPFHh34UN1khVKFdN55e"

    OIDC_CLIENT_SECRETS = "client_secrets.json"
    OIDC_COOKIE_SECURE = False
    OIDC_CALLBACK_ROUTE = "/oidc/callback"
    OIDC_SCOPES = ["openid", "email", "profile"]


class ProdConfig(Config):
    """production specific configuration"""

    FLASK_ENV = "production"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get("PROD_DATABASE_URI")
    SQLALCHEMY_BINDS = {"docs_db": environ.get("PROD_DOCS_DATABASE_URI")}


class DevConfig(Config):
    """development specific configuration"""

    FLASK_ENV = "development"
    # DEBUG = True
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = environ.get("DEV_DATABASE_URI")
    SQLALCHEMY_BINDS = {"docs_db": environ.get("DEV_DOCS_DATABASE_URI")}

    print("dev============================" + SQLALCHEMY_DATABASE_URI)
