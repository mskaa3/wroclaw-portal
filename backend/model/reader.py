from transformers import  pipeline
import os
embed_path_dir=os.path.dirname(os.path.realpath(__file__))
tokenizer_path=os.path.join(embed_path_dir,"bert_tokenizer")
model_path=os.path.join(embed_path_dir,"bert.pt")
# "bert-large-uncased-whole-word-masking-finetuned-squad"
from flask import session
from main import QAmodel,tokenizer

class Reader:
    def __init__(self):
        self.model=QAmodel
        self.tokenizer=tokenizer
        self.question_answerer = pipeline(
            "question-answering", model=self.model, tokenizer=self.tokenizer
        )

    def answer_question(self, question, answer_text):
        return self.question_answerer(question=question, context=answer_text)
