from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import os
embed_path_dir=os.path.dirname(os.path.realpath(__file__))
model_path=os.path.join(embed_path_dir,"Bert")
# "bert-large-uncased-whole-word-masking-finetuned-squad"

class Reader:
    def __init__(self):
        self.model = AutoModelForQuestionAnswering.from_pretrained(
           model_path,low_cpu_mem_usage=True
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,low_cpu_mem_usage=True
        )

        self.question_answerer = pipeline(
            "question-answering", model=self.model, tokenizer=self.tokenizer
        )

    def answer_question(self, question, answer_text):
        return self.question_answerer(question=question, context=answer_text)
