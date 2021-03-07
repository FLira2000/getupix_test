import pymongo
from pymongo import MongoClient

def initialize_collection():
    collection = 0
    try:
        cluster = MongoClient('mongodb+srv://root:root@owid-covid-cluster.ncb4c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        db = cluster['owid-covid-cluster']  
        collection = db['covid_timeseries']
    except:
        print('Erro de servidor.')

    return collection
