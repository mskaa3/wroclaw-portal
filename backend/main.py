"main application configuration"

import os
#from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

# from flask_oidc import OpenIDConnect
# from okta import UsersClient

#load_dotenv(dotenv_path="./.env.local")

DEBUG = bool(os.environ.get("DEBUG", True))

app = Flask(__name__)
CORS(app)

# app.config["OIDC_CLIENT_SECRETS"] = "client_seecrets.json"
# app.config["OIDC_COOKIE_SECURE"] = False
# app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
# app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
# app.config["SECRET_KEY"] = "{{ LONG_RANDOM_STRINGS }}"
# oidc = OpenIDConnect(app)
# app.config["SECRET_KEY"] = "{{ LONG_RANDOM_STRINGS }}"
# okta_client = UsersClient("{{ OKTA_ORG_URL }}", "{{ OKTA_AUTH_TOKEN }}")

app.config["DEBUG"] = DEBUG

# @app.before_request
# def inject_user_into_each_request()
#     if oidc.user_loggedin:
#         g.user = okta_client.get_user(oidc.user_getfield('sub'))
#     else:
#         g.user = None

# @app.route('/greet')
# @oidc.require_login
# def greet():
#     time = datetime.now().hour
#     if time >= 0 and time < 12:
#         return 'Good Morning!'
#     elif time >= 12 and time < 16:
#         return 'Good Afternoon!'
#     else:
#         return 'Good Evening!'
# @app.route('/login')
# @oidc.require_login
# def login():
#     return redirect(url_for('.greet'))
# @app.route('/logout')
# def logout():
#     oidc.logout()
#     return redirect(url_for('.index'))


@app.route("/")
def hello():
    "function for initial testing"
    return "Hello from Wroclaw Portal"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
