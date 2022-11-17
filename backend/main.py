"main application configuration"
from bs4 import BeautifulSoup
import requests
import sqlite3
from googletrans import Translator
# pip installpip
# requests module will be used to CREATE client requests and send them to ANOTHER server
# from crypt import methods
import os, requests
#from dotenv import load_dotenv
from flask import Flask, request, jsonify
import json


# reques object is used to get access to the client request tat is sent TO THE Flask appl from the OTHER clients
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

@app.route("/currency", methods=["GET", "POST"])
def currency_table():
    URL = "https://m.centkantor.pl/"
    page = requests.get(URL)
    URL2 = "http://www.kantorpolonez.pl/"
    page2 = requests.get(URL2)
    URL3 = "https://kantorplex.pl/"
    page3 = requests.get(URL3)

    list_kantorplex_buy = []
    list_kantorplex_sell = []
    list_kantorplex_total = []
    list_kantorplex_result = []

    list_centkantor_names = []
    list_centkantor_buy = []
    list_centkantor_sell = []
    list_centkantor_total = []

    list_kantorpolonez_names = ["USD", "EUR"]
    list_kantorpolonez_buy = []
    list_kantorpolonez_sell = []
    list_kantorpolonez_total = []

    soup = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(page2.content, "html.parser")
    soup3 = BeautifulSoup(page3.content, "html.parser")


    results = soup.find(id="ex_table")
    results2 = soup2.find_all("table")
    results3 = soup3.find_all("table")
    currencies_names = soup.find_all("td", class_="c_symbol")
    currencies_buy = soup.find_all("td", class_= "c_buy")
    currencies_sell = soup.find_all("td", class_= "c_sell")
    currencies_buy2 = soup2.find_all("td", id="K")
    currencies_sell2 = soup2.find_all("td", id="S")
    currencies3 = soup3.find_all("td", class_= "kurs")
    #print(results)

    for value3 in currencies3:
      val = value3
      list_kantorplex_total.append(val.text)

    for value2 in currencies_sell2:
      sell_rate = value2
      comprehended = sell_rate.text.replace("Sprzedaż:", "")
      list_kantorpolonez_sell.append(comprehended)

    for value2 in currencies_buy2:
      buy_rate = value2
      comprehended = buy_rate.text.replace("Kupno:", "")
      list_kantorpolonez_buy.append(comprehended)

    for value1 in currencies_names:
      title_curr = value1
      #buy_rate = value1.find(class_="c_buy")
      #sell_rate = value1.find(class_="c_sell")
      list_centkantor_names.append(title_curr.text)
      #print(title_curr)
      #print(buy_rate)
      #print(sell_rate)
      #print()
    for value1 in currencies_buy:
      buy_rate = value1
      list_centkantor_buy.append(buy_rate.text)
    for value1 in currencies_sell:
      sell_rate = value1
      list_centkantor_sell.append(sell_rate.text)


    list_centkantor_total.append(list_centkantor_names[0])
    list_centkantor_total.append(list_centkantor_buy[0])
    list_centkantor_total.append(list_centkantor_sell[0])
    list_centkantor_total.append(list_centkantor_names[2])
    list_centkantor_total.append(list_centkantor_buy[2])
    list_centkantor_total.append(list_centkantor_sell[2])

    list_kantorpolonez_total.append(list_kantorpolonez_names[1])
    list_kantorpolonez_total.append(list_kantorpolonez_buy[1])
    list_kantorpolonez_total.append(list_kantorpolonez_sell[1])
    list_kantorpolonez_total.append(list_kantorpolonez_names[0])
    list_kantorpolonez_total.append(list_kantorpolonez_buy[0])
    list_kantorpolonez_total.append(list_kantorpolonez_sell[0])

    list_kantorplex_result.append(list_kantorplex_total[0])
    list_kantorplex_result.append(list_kantorplex_total[1])
    list_kantorplex_result.append(list_kantorplex_total[2])
    list_kantorplex_result.append(list_kantorplex_total[3])
    list_kantorplex_result.append(list_kantorplex_total[4])
    list_kantorplex_result.append(list_kantorplex_total[5])

    dict_total = {"centkantor": list_centkantor_total, "kantorpolonez": list_kantorpolonez_total, "kantorplex": list_kantorplex_result}
    #print (list_centkantor_names)
    #print (list_centkantor_buy)
    #print (list_centkantor_sell)
    print (list_centkantor_total)
    #print (results2)
    #print (list_kantorpolonez_buy)
    #print(list_kantorpolonez_sell)
    print (list_kantorpolonez_total)
    #print (list_kantorplex_total)
    print (list_kantorplex_result)
    #jsontest = json.dumps(list_total)
    #print (jsontest)
    #print (type(jsontest))
    #print (jsontest[0])

    return dict_total
    #print(results.prettify())

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
