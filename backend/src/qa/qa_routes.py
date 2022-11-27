
from flask import Blueprint, request, jsonify
import time
from model.retriever import Retriever
from model.reader import Reader
from model.result import Result
qa_routes = Blueprint("qa_routes", __name__)


@qa_routes.route("/qa", methods=["POST"])
def qa():
    st = time.time()
    if request.method == "POST":
        query = request.json["question"]
        reader = Reader()
        retriever = Retriever()
        # retriever.create_embeddings()
        
        answers = {}
        results,links = retriever.retrieve_docs(query)

        for num, i in enumerate(results):
            answers[num] = reader.answer_question(query, i)
        
        final_results={}
        for answer,result,link in zip(answers,results,links):
            answ=answers[answer]['answer']
            score=answers[answer]['score']
            context=result
            ln=link
            res=Result(answ,context,ln,score)
            final_results[answer]=res
        sorted_final=['','','']
        highest=0
        for elem in final_results:
            print(final_results[elem].result_as_dict())
        et = time.time()
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')
        # for num,elem in enumerate(final_results):
        #     if final_results[num].score>highest:
        #         sorted_final[2]=sorted_final[1]
        #         sorted_final[1]=sorted_final[0]
        #         sorted_final[0]=final_results[num]
        #         highest=final_results[num].score

        return jsonify(sorted_final[0]['answer'])


        
        # highest_score = 0
        # best_answer = ""
        # ctx = ""
        # for con, elem in zip(results, answers):
        #     if answers[elem]["score"] > highest_score:
        #         highest_score = answers[elem]["score"]
        #         best_answer = answers[elem]["answer"]
        #         ctx = con
        # print(ctx)
        

