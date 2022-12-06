from transformers import pipeline
import os
from main import QAmodel, tokenizer


class Reader:
    def __init__(self):
        self.model = QAmodel
        self.tokenizer = tokenizer
        self.question_answerer = pipeline(
            "question-answering", model=self.model, tokenizer=self.tokenizer
        )

    def answer_question(self, question, answer_text):
        return self.question_answerer(question=question, context=answer_text)
