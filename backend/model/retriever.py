from pathlib import Path
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import faiss
import numpy as np
import time
import os
import pickle


dirname ='.\\backend\\model\\docs\\'
ext = ('txt')
threshold = 250

    
class Retriever():
  def __init__(self):
    self.model=SentenceTransformer('sentence-transformers/LaBSE')
    self.tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/LaBSE')

 


  def create_embeddings(self):
    content_divided=[]
    for files in os.listdir(dirname):
      if files.endswith(ext):
          print(files)
          file=open(os.path.join(dirname, files), "r",encoding="utf-8")
          content=file.read()
          # for chunk in content.split('. '):
          #     if content_divided and len(chunk)+len(content_divided[-1]) < threshold:
          #        content_divided[-1] += ' '+chunk+'.'
          #     else:
          #        content_divided.append(chunk+'.')
          ct_list=content.split(' ')
          temp_paragraph=''
          for i,chunk in enumerate(ct_list):
              if i!=0 and i%150==0:
                  content_divided.append(temp_paragraph)
                  temp_paragraph=''
              else:
                  temp_paragraph=temp_paragraph+' '+chunk

          content_divided.append(temp_paragraph)
      else:
          continue
      self.paragraphs=content_divided
      embeddings = self.model.encode(content_divided)  
      with open('.\\backend\\model\\embeddings.pkl', "wb") as fOut:
          pickle.dump({'sentences': content_divided, 'embeddings': embeddings}, fOut, protocol=pickle.HIGHEST_PROTOCOL)
      
# najpeirw elastic search na np 20 zapytań a potem sentence-transformer

  def retrieve_docs(self,query):

    with open('.\\backend\\model\\embeddings.pkl', "rb") as fIn:
        stored_data = pickle.load(fIn)
        content = stored_data['sentences']
        embeddings = stored_data['embeddings']

    index = faiss.IndexIDMap(faiss.IndexFlatIP(768))
    index.add_with_ids(embeddings, np.array(range(0, len(content))).astype(np.int64))
    t=time.time()
    query_vector = self.model.encode([query])
    k = 5
    top_k = index.search(query_vector, k)
    print('totaltime: {}'.format(time.time()-t))
    return [content[_id] for _id in top_k[1].tolist()[0]]

    # query=str("Can students work while studying?")
    # query=str("Is there a cinema for foreigners?")
    # query=str("When I sent document by post I need to come in person to have my fingerprints taken")
    # results=search(query)
    # print('results :')
    # for result in results:
    #    print('\t',result)

 