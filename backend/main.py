"""Flask app factory"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow
import connexion

from src.uni.data_loader import fill_tables
from database import Database


# from flask_oidc import OpenIDConnect
# from okta.client import Client as UsersClient


# Globally accessible libraries
# db = SQLAlchemy()
db = Database()
migrate = Migrate()
ma = Marshmallow()


def create_app(config_class="config.DevConfig"):
    "initiate core application"
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config_class)
    print(app.config["DEBUG"])

    CORS(app)
    api = Api(app)

    """initialize plugins"""
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    with app.app_context():
        # include routes
        # from . import routes
        # from src.uni.resources.uni_routes import Vo
        from src.uni.routes.voivodeship_routes import (
            VoivodeshipIdApi,
            # VoivodeshipNameApi,
            VoivodeshipsApi,
        )

        from src.uni.routes.course_routes import (
            CourseIdApi,
            CourseNameApi,
            CoursesApi,
        )

        from src.uni.routes.uni_routes import (
            UniIdApi,
            UniUidApi,
            UniNameApi,
            UnisApi,
            CitiesApi,
        )

        from src.uni.routes.discipline_routes import (
            DisciplineIdApi,
            DisciplineNameApi,
            DisciplinesApi,
        )

        from src.uni.routes.level_routes import (
            CourseLevelIdApi,
            CourseLevelNameApi,
            CourseLevelsApi,
        )

        from src.uni.routes.search_routes import SearchUniApi, SearchCourseApi

        api.add_resource(VoivodeshipIdApi, "/voivodeships/<id>")
        # api.add_resource(VoivodeshipNameApi,'/voivodeships/<name>')
        api.add_resource(VoivodeshipsApi, "/voivodeships")

        api.add_resource(DisciplineIdApi, "/disciplines/<discipline_id>")
        api.add_resource(DisciplineNameApi, "/disciplines/name/<disciline_name>")
        api.add_resource(DisciplinesApi, "/disciplines")

        api.add_resource(CourseIdApi, "/courses/<course_id>")
        api.add_resource(CourseNameApi, "/courses/name/<course_name>")
        api.add_resource(CoursesApi, "/courses")

        api.add_resource(UniIdApi, "/unis/<uni_id>")
        api.add_resource(UniUidApi, "/unis/uid/<uni_uid>")
        api.add_resource(UniNameApi, "/unis/name/<uni_name>")
        api.add_resource(UnisApi, "/unis")
        api.add_resource(CitiesApi, "/unis/cities")

        api.add_resource(CourseLevelIdApi, "/courses/levels/<level_id>")
        api.add_resource(CourseLevelNameApi, "/courses/levels/name/<level_name>")
        api.add_resource(CourseLevelsApi, "/courses/levels")

        api.add_resource(
            SearchUniApi,
            "/search/unis",
        )
        api.add_resource(
            SearchCourseApi,
            "/search/courses",
        )

        # from src.uni.models.uni_model import Uni
        # from src.uni.models.voivodeship_model import Voivodeship

        # db.create_all()
        print("db=====================================================")
        print(db.engine.url.database)

        # @app.before_first_request
        # def create_tables():
        # db.Base.metadata.create_all(bind=db.engine)
        # fill_tables(db.engine.url.database)

    return app


# @app.before_first_request
# @with_appcontext
# def create_tables():
#    db.create_all()

"""

app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = "super secret"
oidc = OpenIDConnect(app)
# app.config["SECRET_KEY"] = "{{ LONG_RANDOM_STRINGS }}"
# okta_client = UsersClient("{{ OKTA_ORG_URL }}", "{{ OKTA_AUTH_TOKEN }}")
okta_client = UsersClient(
    {
        "orgUrl": "https://dev-73352242.okta.com/",
        "token": "00wypJxwIxxILACoZp3bnbxPFHh34UN1khVKFdN55e",
    }
)
# okta_client = UsersClient(
#    os.environ.get("OKTA_ORG_URL"), os.environ.get("OKTA_AUTH_TOKEN")
# )
# okta_client = UsersClient(app.config["OKTA_ORG_URL"], app.config["OKTA_AUTH_TOKEN"])

# app.config["DEBUG"] = DEBUG


@app.before_request
def inject_user_into_each_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None
    print(g.user)


# @app.route("/greet")
# @oidc.require_login
def greet():
    time = datetime.now().hour
    if time >= 0 and time < 12:
        return "Good Morning!"
    if time >= 12 and time < 16:
        return "Good Afternoon!"

    return "Good Evening!"


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for(".greet"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".index"))


# api.add_resource(UniList, '/unis')


@app.route("/")
def index():
    "function for initial testing"
    return "Hello from Wroclaw Portal"


"""
