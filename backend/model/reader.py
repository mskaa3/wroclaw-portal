from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch 

class Reader():
   def __init__(self):
        self.model=AutoModelForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        self.tokenizer = AutoTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
   
   def answer_question(self,question, answer_text):

        # input_ids = QAtokenizer.encode(question, answer_text, max_length=512)
        input_ids = self.tokenizer.encode(question, answer_text, max_length=512, truncation=True)
        
        # ======== Set Segment IDs ========
        # Search the input_ids for the first instance of the `[SEP]` token.
        sep_index = input_ids.index(self.tokenizer.sep_token_id)

        # The number of segment A tokens includes the [SEP] token istelf.
        num_seg_a = sep_index + 1

        # The remainder are segment B.
        num_seg_b = len(input_ids) - num_seg_a

        # Construct the list of 0s and 1s.
        segment_ids = [0]*num_seg_a + [1]*num_seg_b

        # There should be a segment_id for every input token.
        assert len(segment_ids) == len(input_ids)

        outputs = self.model(torch.tensor([input_ids]), # The tokens representing our input text.
                        # token_type_ids=torch.tensor([segment_ids]), # The segment IDs to differentiate question from answer_text
                        return_dict=True) 

        start_scores = outputs.start_logits
        end_scores = outputs.end_logits

        # ======== Reconstruct Answer ========
        # Find the tokens with the highest `start` and `end` scores.
        answer_start = torch.argmax(start_scores)
        answer_end = torch.argmax(end_scores)

        # Get the string versions of the input tokens.
        tokens = self.tokenizer.convert_ids_to_tokens(input_ids)

        # Start with the first token.
        answer = tokens[answer_start]

        # Select the remaining answer tokens and join them with whitespace.
        for i in range(answer_start + 1, answer_end + 1):
            
            # If it's a subword token, then recombine it with the previous token.
            if tokens[i][0:2] == '##':
                answer += tokens[i][2:]
            
            # Otherwise, add a space then the token.
            else:
                answer += ' ' + tokens[i]

        print('Answer: "' + answer + '"')
        return answer


    # for i in results:
    #         answer_question(query,i)
    #         print ("Reference Document: ", i)
    #         print("next")