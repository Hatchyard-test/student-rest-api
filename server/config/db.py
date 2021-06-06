from pymongo import MongoClient
from .config import MONGO_URI

#setup mongodb connection with docker
conn = MongoClient(host='mongohost', port=27017)

#setup mongodb connection in local
#conn = MongoClient(MONGO_URI)