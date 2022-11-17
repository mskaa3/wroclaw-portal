import sqlite3
from flask import Blueprint, request, jsonify
from googletrans import Translator
from model.retriever import Retriever
from model.reader import Reader

docs_routes = Blueprint("docs_routes", __name__)


@docs_routes.route("/qa", methods=["POST"])
def qa():
    if request.method == "POST":
        query = request.json["question"]
        reader = Reader()
        retriever = Retriever()
        # retriever.create_embeddings()
        answers = {}
        results = retriever.retrieve_docs(query)
        for num, i in enumerate(results):
            answers[num] = reader.answer_question(query, i)
        highest_score = 0
        best_answer = ""
        ctx = ""
        for con, elem in zip(results, answers):
            if answers[elem]["score"] > highest_score:
                highest_score = answers[elem]["score"]
                best_answer = answers[elem]["answer"]
                ctx = con
        print(ctx)
        return jsonify(best_answer)


@docs_routes.route("/")
def docs():
    with sqlite3.connect("docs_db.db") as conn:
        try:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM categories")
            categories_data = cur.fetchall()
            cur.execute(f"SELECT * FROM documents")
            documents_data = cur.fetchall()
            return jsonify(categories_data, documents_data)
        except sqlite3.Error as er:
            return er
