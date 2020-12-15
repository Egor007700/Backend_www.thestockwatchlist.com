import requests
from pymongo import MongoClient

url = "https://financialmodelingprep.com/api/v3/quotes?apikey=525f52f4ab862d8f9dd17476d613de0a"
response = requests.get(url)