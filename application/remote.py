import pymongo
from pymongo import MongoClient
from setup import initialize_collection

cluster = MongoClient('mongodb+srv://root:root@owid-covid-cluster.ncb4c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['owid-covid-cluster']

collection = []
try:
    collection = db['covid_timeseries']
except:
    initialize_collection() # TODO


def find_one(data):
    return collection.find_one(data)

def find_various(data):
    pass

def insert_one(data):
    pass

def insert_multiple(data):
    pass

def alter(data):
    pass

def delete(data):
    pass

