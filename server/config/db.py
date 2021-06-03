from pymongo import MongoClient
from .config import MONGO_URI

#setup mongodb connection
conn = MongoClient(MONGO_URI)