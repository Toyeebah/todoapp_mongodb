from pymongo import mongo_client
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_DB_CONNECTION_URI = os.environ.get('MONGO_DB_CONNECTION_URI')


client = mongo_client.MongoClient(MONGO_DB_CONNECTION_URI)

user_collection = client["todoapp"]["users"]
todo_collection = client["todoapp"]["todo"]



try:
    client.admin.command('ping')
    print("Pinging your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)