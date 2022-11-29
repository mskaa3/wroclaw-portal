
import faiss
import numpy as np
import os
import pickle
import pandas as pd
from rank_bm25 import BM25Okapi
from gensim.parsing.preprocessing import preprocess_string
from main import sentence_model


dirname = ".\\backend\\model\\docs\\"
ext = "txt"

embed_path_dir=os.path.dirname(os.path.realpath(__file__))
embed_path=os.path.join(embed_path_dir, "embeddings.pkl")
corpus_path=os.path.join(embed_path_dir,"corpus.csv")
model_path=os.path.join(embed_path_dir,"labse.pt")

class Retriever:
    def __init__(self):
            
            self.model=sentence_model

    def create_embeddings(self):
        df = pd.read_csv(corpus_path, encoding='latin-1',sep=';')
        content_divided=df['content'].tolist()
        indexes=list(range(0, len(content_divided)))
        embeddings = self.model.encode(content_divided)
        with open(embed_path, "wb") as fOut:
                 pickle.dump({'paragraphs': content_divided, 'embeddings': embeddings, 'indexes':indexes}, fOut, protocol=pickle.HIGHEST_PROTOCOL)
        return True

    def retrieve_docs(self, query):
        df = pd.read_csv(corpus_path, encoding='latin-1',sep=';')
        meta_df_tokens = df.content.fillna('').apply(preprocess_string)
        bm25_index = BM25Okapi(meta_df_tokens.tolist())
        # found_indexes = self.search(num_results=10,search_string=meta_df_tokens,bm25_index=bm25)
        search_tokens = preprocess_string(query)
        scores = bm25_index.get_scores(search_tokens)
        top_indexes = np.argsort(scores)[::-1][:10]
        filtered_content=[]
        new_index_to_old={}
        filtered_embeddings=np.zeros((len(top_indexes), 768))
        
        with open(embed_path, "rb") as fIn:
            stored_data = pickle.load(fIn)
            content_divided = stored_data['paragraphs']
            embeddings = stored_data['embeddings']
            sentence_indexes=stored_data['indexes']

        for num,index in enumerate(top_indexes):
            filtered_content.append(content_divided[index])
            new_index_to_old[num]=index
            filtered_embeddings[num]=embeddings[index]

        index = faiss.IndexIDMap(faiss.IndexFlatIP(768))
        index.add_with_ids(filtered_embeddings, np.array(range(0, len(filtered_content))).astype(np.int64))
        
        # t = time.time()
        # print("totaltime: {}".format(time.time() - t))
        query_vector = self.model.encode([query])
        k = 3
        top_k = index.search(query_vector, k)
        res=[filtered_content[_id] for _id in top_k[1].tolist()[0]]
        res_index=[filtered_content.index(filtered_content[_id]) for _id in top_k[1].tolist()[0]]
        final_idx=[]
        final_links=[]
        for index in res_index:
            final_idx.append(new_index_to_old[index])
        for index in final_idx:
            final_links.append(df['source_link'].values[index])
        return res,final_links
 

    def search(search_string,bm25_index, num_results):
        search_tokens = preprocess_string(search_string)
        scores = bm25_index.get_scores(search_tokens)
        top_indexes = np.argsort(scores)[::-1][:num_results]
        return top_indexes
