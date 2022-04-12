from pymongo import MongoClient
mongo_client = MongoClient('mongodb://mongo:27017/')
QUIZ_DB = mongo_client['quiz']
QUIZ_COL = QUIZ_DB['quiz']
