
from flask import Blueprint, request, jsonify

from model.retriever import Retriever
from model.reader import Reader

qa_routes = Blueprint("qa_routes", __name__)


@qa_routes.route("/qa", methods=["POST"])
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

