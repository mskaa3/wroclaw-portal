from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline


class Reader:
    def __init__(self):
        self.model = AutoModelForQuestionAnswering.from_pretrained(
            "bert-large-uncased-whole-word-masking-finetuned-squad"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(
            "bert-large-uncased-whole-word-masking-finetuned-squad"
        )
        self.question_answerer = pipeline(
            "question-answering", model=self.model, tokenizer=self.tokenizer
        )

    def answer_question(self, question, answer_text):
        return self.question_answerer(question=question, context=answer_text)
