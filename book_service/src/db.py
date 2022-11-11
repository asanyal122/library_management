from flask import Flask
from flask_pymongo import pymongo



CONNECTION_STRING = "mongodb+srv://asanyal122:arunjyoT1@ecommercecluster.fpcxf.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('test')
books_collection = pymongo.collection.Collection(db, 'books')


