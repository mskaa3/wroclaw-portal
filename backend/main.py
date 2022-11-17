"""Flask app factory"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_marshmallow import Marshmallow
import connexion

from src.uni.data_loader import fill_tables
from src.forum.forum_sample_data import fill_forum_tables
from database import Database

from bs4 import BeautifulSoup
import requests
import sqlite3
from googletrans import Translator
# pip installpip
# requests module will be used to CREATE client requests and send them to ANOTHER server
# from crypt import methods
import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import json



from model.retriever import Retriever
from model.reader import Reader

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

        from src.forum.routes.topic_routes import (
            TopicIdApi,
            TopicNameApi,
            TopicsApi,
        )

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

        api.add_resource(TopicIdApi, "/forum/topics/<topic_id>")
        api.add_resource(TopicNameApi, "/forum/topics/name/<topic_name>")
        api.add_resource(TopicsApi, "/forum/topics")

        # from src.uni.models.uni_model import Uni
        # from src.uni.models.voivodeship_model import Voivodeship

        # db.create_all()
        print("db=====================================================")
        print(db.engine.url.database)

        # @app.before_first_request
        # def create_tables():
        # db.Base.metadata.create_all(bind=db.engine)
        # fill_tables(db.engine.url.database)

        # db.Base.metadata.reflect(db.engine)
        # db.Base.metadata.tables["users"].create(bind=db.engine)
        # db.Base.metadata.tables["topics"].create(bind=db.engine)
        # db.Base.metadata.tables["threads"].create(bind=db.engine)
        # db.Base.metadata.tables["posts"].create(bind=db.engine)
        # fill_forum_tables(db.engine.url.database)

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




@app.route("/")
def index():
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
