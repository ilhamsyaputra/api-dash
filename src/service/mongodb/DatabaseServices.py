import os
from dotenv import load_dotenv
from pymongo import MongoClient

class DatabaseServices(object):
    load_dotenv()

    # credential information
    MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')
    MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')
    MONGODB_HOST = os.environ.get('MONGODB_HOST')

    URI = f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@{MONGODB_HOST}'
    DATABASE = None

    def connect():
        '''
        method to connect to database
        take a look at client.Seispro, change 'SeisPro' to your database name
        '''
        client = MongoClient(DatabaseServices.URI)
        DatabaseServices.DATABASE = client.SeisPro

    def find(query: dict):
        '''
        method to find document
        '''
        DatabaseServices.connect()
        return DatabaseServices.DATABASE.dashboard.find_one(query)
