# 
# using following Data have to build reccomendation system
# Each should have 1000 entries
# 1. user[uid , location, gender , Age , signup_date , last_active_date]
# 2. Products[pid , category  , price , brand  , description , Rating , Reviews ]
# 3. Transaction[tid , uid , pid , transactionAmount , transactionDate , transactionTime , transactionLocation , transactionDevice]
# 4. interaction[uid , pid , stalk_time , wishtlisted , addCart-nobuy]


# Get Data from flipkart Website using Scrapy
# 1. Product Data
# 2. User Data
# 3. Transaction Data
# 4. Interaction Data


# Using the above data build a recommendation system
# Library to be used : Surprise Library (SVD , SVD++ , NMF , KNN , KNNBaseline , KNNBasic , KNNWithMeans , KNNWithZScore , BaselineOnly , CoClustering)
# Tensorflow Recommenders

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from sklearn.metrics.pairwise import pairwise_distances

# tensorflow Recommenders
import tensorflow as tf
import tensorflow_recommenders as tfrs


# Surprise Library
from surprise import Reader, Dataset
from surprise.model_selection import cross_validate
from surprise import SVD, SVDpp, NMF, KNNBaseline, KNNBasic, KNNWithMeans, KNNWithZScore, BaselineOnly, CoClustering
from surprise.model_selection import train_test_split

# import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy import Spider
from scrapy import Request

# We need to implement following use cases
# 1. User Based Recommendation System i.e based on user history and interaction with products we have to recommend products to user
# 2. Demographic Based Recommendation System i.e based on user demographic data we have to recommend products to user
# 3. collaborative filtering Recommendation System i.e based similar users and similar products we have to recommend products to user



def getRecommendation():

    # using tensorflow Recommenders
    tfrec = tf.data.Dataset.from_tensor_slices((df_interaction['uid'].values, df_interaction['pid'].values))
    tfrec = tfrec.map(lambda x,y: {
        "uid": x,
        "pid": y
    })
    tfrec = tfrec.batch(1024)
    cached = tfrec.cache()
    tffm = tfrs.models.FactorizationMachines(
        task = tfrs.tasks.Ranking(
            loss = tf.keras.losses.MeanSquaredError(),
            metrics = [tf.keras.metrics.RootMeanSquaredError()]
        ),
        embedding_dimension = 32,
        l2_regularization = 0.1
    )
    tffm.fit(cached, epochs = 10)
    tffm.evaluate(cached, return_dict = True)
    tffm.predict(cached)

    # using surprise library
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df_interaction[['uid', 'pid', 'stalk_time']], reader)
    trainset, testset = train_test_split(data, test_size=.25)
    algo = SVD()
    algo.fit(trainset)
    predictions = algo.test(testset)
    cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    uid = str(196)
    iid = str(302)
    pred = algo.predict(uid, iid, verbose=True)
    
    # using cosine similarity
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df_product['description'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    indices = pd.Series(df_product.index, index=df_product['pid']).drop_duplicates()
    get_recommendations(196, cosine_sim)


    return df_product.head(10)
