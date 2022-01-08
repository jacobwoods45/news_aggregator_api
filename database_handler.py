
from pymongo import MongoClient

client = MongoClient('mongodb+srv://jacobwoods45:Sharpie78!@newsaggregatorcluster.ncifr.mongodb.net/NewsAggregator?retryWrites=true&w=majority')
db = client["NewsAggregator"]
clips = db["NewsClips"]

def get_all_news_clips():
    cursor = clips.find({})
    for document in cursor:
          print(document)


get_all_news_clips