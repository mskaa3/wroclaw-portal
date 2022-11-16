"main application configuration"
import json
import sqlite3

# pip installpip
# requests module will be used to CREATE client requests and send them to ANOTHER server
# from crypt import methods
import os, requests
#from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.retriever import Retriever
from model.reader import Reader
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
        # return jsonify([uni for uni in unis])
        return jsonify(unis)
    if request.method == "POST":
        # save
        return {}


@app.route("/qa",methods=["POST"])
def qa():
    if request.method == 'POST':
        query=request.json["question"]
        reader=Reader()
        retriever=Retriever()
        # retriever.create_embeddings()
        answers={}
        results=retriever.retrieve_docs(query)
        for num,i in enumerate(results):
            answers[num]=reader.answer_question(query,i)
        highest_score=0
        best_answer=''
        ctx=''
        for con,elem in zip(results,answers):
            if answers[elem]['score']>highest_score:
                highest_score=answers[elem]['score']
                best_answer=answers[elem]['answer']
                ctx=con
        print(ctx)      
        return jsonify(best_answer)

 


@app.route("/docs")
def docs():
    with sqlite3.connect('docs_db.db') as conn:
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM categories")
            categories_data = cur.fetchall()
            cur.execute(f"SELECT * FROM documents")
            documents_data = cur.fetchall()
            return jsonify(categories_data,documents_data)
        except sqlite3.Error as er:
            return er



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
