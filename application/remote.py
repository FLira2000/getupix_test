#import pymongo
from setup import initialize_collection

collection = initialize_collection()

def find_one(data):
    return collection.find_one(data)

def find_various(data):
    pass

def insert_one(data):
    collection.insert_one(data)

def insert_multiple(data):
    pass

def alter(data):
    pass

def delete(data):
    pass

