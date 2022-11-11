"main application configuration"
import json
from bs4 import BeautifulSoup
import requests
from googletrans import Translator
# pip installpip
# requests module will be used to CREATE client requests and send them to ANOTHER server
# from crypt import methods
import os, requests
#from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.retriever import Retriever
from model.reader import Reader
# from docs_database import Category, Documents,db
# from flask_oidc import OpenIDConnect
# from okta import UsersClient

#load_dotenv(dotenv_path="./.env.local")

DEBUG = bool(os.environ.get("DEBUG", True))

app = Flask(__name__)
# CORS(app)

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


@app.route("/qa")
def generate_answer():
    query="Is there any cinema for foreigners?"
    results_dict={}
    reader=Reader()
    retriever=Retriever()
    retriever.create_embeddings()
    
    results=retriever.retrieve_docs(query)
    for num,i in enumerate(results):
        answer=reader.answer_question(query,i)
        results_dict[num]=answer
    return results_dict
 


# @app.route("/docs")
# def docs_list():

#         translator = Translator()
#         page = requests.get('https://przybysz.duw.pl/en/documents-to-download/',verify=False)   
#         soup = BeautifulSoup(page.text, 'html.parser')


#         headers=[]
#         head = soup.find_all('h4', attrs = {'class':''}) 
#         for elem in head:
#             elem_fixed=(elem.text).replace('\n\t\t\t\t','')
#             headers.append(elem_fixed.replace('\n\t\t\t',''))
#         headers.append("Others")
#         categories = soup.find_all("div", class_="frame frame-default frame-type-uploads frame-layout-0")
#         categories.pop(0)
#         # result_dict={}
#         big_dict=[]
#         i=1
#         for header,category in zip(headers,categories):
#             dict={}
#             experiment={}
#             experiment["id"]=i
#             experiment["category"]=header


#             for row in category.find_all('div', attrs = {'class':''}) :
#                 doc_title = translator.translate(row.span.text,src='pl',dest='en')
#                 dict[doc_title.text]='https://przybysz.duw.pl'+row.a['href']
#                 experiment["content"]=dict
#             big_dict.append(experiment)
#             # result_dict[header]=dict
#             i=i+1
            
#             for key in big_dict:
#                 cat = Category(category_name=key)
#                 db.session.add(cat)
#                 db.session.commit()
#                 for name in big_dict[key]:
#                     docs=Documents(link=big_dict[key][name],link_name=name,category=cat.id)
#                     db.session.add(docs)
#                     db.session.commit()
#         return big_dict



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
