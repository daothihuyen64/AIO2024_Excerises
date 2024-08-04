import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_search ( question , tfidf_vectorizer , top_d =5) :
    question = question.lower()
    query_embedded = tfidf_vectorizer.transform([question])
    cosine_scores = cosine_similarity(query_embedded, tfidf_vectorizer.transform(context)).flatten()

    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores.argsort()[ - top_d :][:: -1]:
        doc_score = {
            'id': idx ,
            'cosine_score': cosine_scores [ idx ]
        }
        results . append ( doc_score )
    return results

def corr_search ( question , tfidf_vectorizer , top_d =5) :
    # lowercasing before encoding
    question = question.lower()
    query_embedded = tfidf_vectorizer.transform([question])
    context_embedded = tfidf_vectorizer.transform(context).toarray()
    corr_scores =  np.corrcoef(query_embedded.toarray(), context_embedded)
    corr_scores = corr_scores [0][1:]
    # Get top k correlation score and index its
    results = []
    for idx in corr_scores . argsort () [ - top_d :][:: -1]:
        doc = {
            'id': idx ,
            'corr_score': corr_scores [ idx ]
        }
        results . append ( doc )
    return results



vi_data_df = pd.read_csv("Q10_advertising.csv")
context = vi_data_df ['text']
context = [ doc.lower () for doc in context ]

# Q10
tfidf_vectorizer = TfidfVectorizer ()
context_embedded = tfidf_vectorizer.fit_transform(context)
#print(context_embedded.toarray()[7][0])

# Q11
question = vi_data_df . iloc [0][ 'question']
results = tfidf_search ( question , tfidf_vectorizer , top_d =5)
#print(results[0]['cosine_score'])

# Q12
question = vi_data_df . iloc [0][ 'question']
results = corr_search ( question , tfidf_vectorizer , top_d =5)
print(results[1][ 'corr_score'])