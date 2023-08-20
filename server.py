
import pickle
import pandas as pd
import numpy as np
# import fastapi
from fastapi import FastAPI
from gensim.models import Word2Vec




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



def getreccomendation(userId , prod2vecRecom , new_transaction_table , pidToProductMetadata):
    reccomdations = []

    pastPurchases = new_transaction_table[new_transaction_table['UID'] == userId]['sequence'].values

    reccomdations = prod2vecRecom.model.wv.most_similar(positive=pastPurchases[0], topn=10)

    reccomdation = []
    for i in reccomdations:
        reccomdation.append(pidToProductMetadata[i[0]])

        
    return reccomdation


# Load the model
prod2vecRecom = pickle.load(open('prod2vec.pkl', 'rb'))
# print vocab


# Load the data

products = pd.read_csv(r'.\Recommeder\Data\flipkart_com-ecommerce_sample.csv')
print(products.shape ,len(products['product_name'].unique()),len(products['uniq_id'].unique()))

transactions_path = r".\Recommeder\Data\transaction.csv"
transaction_table = pd.read_csv(transactions_path)

pidToProductMetadata = {}
for i in range(len(products)):
    pidToProductMetadata[products['uniq_id'][i]] = [products['product_name'][i],products['description'][i],products['product_category_tree'][i],products['brand'][i],products['product_url'][i],products['image'][i]]
pidToProductSeries = pd.Series(products['product_name'].values,index=products['uniq_id']).to_dict()

new_transaction_table = pd.read_csv(r'.\Recommeder\Data\new_transaction_table.csv')


# testing model
userId = "2e112284-8013-430d-b784-8f1808dd4e76"

print("User ID: ", userId)

reccomdations = getreccomendation(userId , prod2vecRecom , new_transaction_table , pidToProductMetadata)
print(reccomdations)