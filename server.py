
import pickle
import pandas as pd
import numpy as np
# import fastapi
from fastapi import FastAPI
from gensim.models import Word2Vec

import json



class Prod2VecRecommender():
    def __init__(self, min_count=2, size=100, window=5, decay_alpha=0.9, workers=4):

        super(Prod2VecRecommender, self).__init__()
        self.min_count = min_count
        self.size = size
        self.window = window
        self.decay_alpha = decay_alpha
        self.workers = workers

    def __str__(self):
        return 'Prod2VecRecommender(min_count={min_count}, ' \
               'size={size}, ' \
               'window={window}, ' \
               'decay_alpha={decay_alpha}, ' \
               'workers={workers})'.format(**self.__dict__)

    def fit(self, train_data):
        sequences = train_data['sequence']
        self.model = Word2Vec(sentences=sequences, vector_size=self.size, window=self.window, min_count=self.min_count, workers=self.workers, sg=0)
        self.model.train(sequences, total_examples=len(sequences), epochs=100)
        return self


prod2vecRecom = pickle.load(open('prod2vec.pkl', 'rb'))



new_transaction_table = pd.read_csv(r'.\Recommeder\Data\new_transaction_table.csv')
for i in range(len(new_transaction_table)):
    new_transaction_table['sequence'][i] = new_transaction_table['sequence'][i].replace("[","").replace("]","").replace("'","").split(", ")



# userId = "2e112284-8013-430d-b784-8f1808dd4e76"

# print("User ID: ", userId)
pidToProductMetadata = json.load(open(r'.\Recommeder\Data\pidToProductMetadata.json', 'r'))
# reccomdations = getreccomendation(userId , prod2vecRecom , new_transaction_table , pidToProductMetadata)

def getreccomendation(userId ):
    reccomdations = []
    

    pastPurchases = new_transaction_table[new_transaction_table['UID'] == userId]['sequence']

    pastPurchases = pastPurchases.tolist()[0]
    # print(pastPurchases , type(pastPurchases))
    reccomdations = prod2vecRecom.model.wv.most_similar(positive=pastPurchases[0], topn=10)

    reccomdation = []
    for i in reccomdations:
        reccomdation.append(pidToProductMetadata[i[0]])


    return reccomdation


# print(reccomdations)


app = FastAPI()


@app.get("/reccomend/{userId}")
def get_reccomendation(userId: str):
    return getreccomendation(userId )


