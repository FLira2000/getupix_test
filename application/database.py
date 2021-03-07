from pymongo import MongoClient
from data_preparation import transform_csv, get_csv, series_handler
from progressbar import progressbar

def initialize_database():
    database = None
    try:
        cluster = MongoClient('mongodb+srv://root:root@owid-covid-cluster.ncb4c.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        database = cluster['owid-covid-cluster'] 
    except Exception as e:
        print(e)

    return database

def initialize_collection(database = initialize_database()):
    collection = None
    try:
        collection = database['covid_timeseries']
    except Exception as e:
        print(e)

    return collection

def create_collection():
    database = initialize_database()
    try:
        if database == None:
            raise ConnectionError

        database['covid_timeseries'].drop()
        collection = initialize_collection(database)

        df = transform_csv(get_csv())
        #depois das analises, podemos separar cada location em um document
        locations = df.location.unique()
        for l in progressbar(locations):
            tmp = series_handler(df.loc[df['location'] == l])
            collection.insert_one(tmp)
    except Exception as e:
        print(e)