# requests module will be used to CREATE client requests and send them to ANOTHER server
# from crypt import methods
import os
import json

# import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify, g
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from datetime import datetime

# reques object is used to get access to the client request
# that is sent TO THE Flask appl from the OTHER clients
from flask_cors import CORS
from flask_oidc import OpenIDConnect

# from okta import UsersClient
from okta.client import Client as UsersClient


# def create_app():
load_dotenv(dotenv_path="./.env.local")

# DEBUG = bool(os.environ.get("DEBUG", True))

app = Flask(__name__)
CORS(app)

app.config.from_object("config")

# api = Api(app)

uni_db = SQLAlchemy(app)
migrate = Migrate(app, uni_db)

uni_db.init_app(app)
migrate.init_app(app, uni_db)


app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = "super secret"
app.config["OKTA_ORG_URL"] = "https://dev-73352242.okta.com/"
app.config["OKTA_AUTH_TOKEN"] = "00wypJxwIxxILACoZp3bnbxPFHh34UN1khVKFdN55e"

oidc = OpenIDConnect(app)

okta_client = UsersClient(
    {
        "orgUrl": "https://dev-73352242.okta.com/",
        "token": "00wypJxwIxxILACoZp3bnbxPFHh34UN1khVKFdN55e",
    }
)
# (app.config["OKTA_ORG_URL"], app.config["OKTA_AUTH_TOKEN"])


@app.before_request
def inject_user_into_each_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None
    print(g.user)


@app.route("/")
def hello():
    "function for initial testing"
    return "Hello from Wroclaw Portal"


@app.route("/unis", methods=["GET", "POST"])
def unis_list():
    "get univercity list"
    # uniSearchWord=request.args.get("query")
    if request.method == "GET":
        # read
        # unis=unis_collection.find({})
        # return jsonify([uni for uni in unis ])
        unis = [
            {
                "id": 1,
                "title": "Uni 1",
                "logo": "https://avatars.mds.yandex.net/i?id=3879b1e342099fb44cbf3565b1e6f384-5313761-images-thumbs&n=13",
                "site": "https://pwr.edu.pl/",
            },
            {
                "id": 2,
                "title": "Uni 2",
                "logo": "https://cdn11.bigcommerce.com/s-7va6f0fjxr/images/stencil/1280x1280/products/60361/76600/Hello-Kitty-With-Gun-Decal__92727.1506656896.jpg?c=2&imbypass=on",
                "site": "https://www.igig.up.wroc.pl/en/",
            },
        ]

        return jsonify(unis)

    if request.method == "POST":
        # save
        return {}


@app.route("/search/unis", methods=["GET", "POST"])
def unis_search_list():
    "get univercity list"
    # uniSearchWord=request.args.get("query")
    if request.method == "GET":
        # read
        # unis=unis_collection.find({})
        # return jsonify([uni for uni in unis ])
        uniss = [
            {
                "id": 1,
                "title": "Uni 1",
                "logo": "https://avatars.mds.yandex.net/i?id=3879b1e342099fb44cbf3565b1e6f384-5313761-images-thumbs&n=13",
                "site": "https://pwr.edu.pl/",
            },
            {
                "id": 2,
                "title": "Uni 2",
                "logo": "https://cdn11.bigcommerce.com/s-7va6f0fjxr/images/stencil/1280x1280/products/60361/76600/Hello-Kitty-With-Gun-Decal__92727.1506656896.jpg?c=2&imbypass=on",
                "site": "https://www.igig.up.wroc.pl/en/",
            },
        ]
        # return jsonify([uni for uni in unis])
        query_param = request.args.get("q")
        if query_param is None:
            filtered_unis = uniss
        else:
            filtered_unis = list(filter(lambda x: x["id"] == int(query_param), uniss))
        # filtered_unis = [uni for uni in unis if uni["id"] == int(query_param)]

        # return jsonify(unis)
        return jsonify(filtered_unis)
    if request.method == "POST":
        # save
        return {}


@app.route("/greet", methods=["GET"])
@oidc.require_login
def greet():
    time = datetime.now().hour
    if time >= 0 and time < 12:
        return "Good Morning!"
    if time >= 12 and time < 16:
        return "Good Afternoon!"

    return "Good Evening!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
