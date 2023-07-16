# app/database/database.py

from pymongo import MongoClient
from bson.objectid import ObjectId

# Load environment variables
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

client = MongoClient(DATABASE_URL)

db = client.get_database('tinybug_db')
collection = db.get_collection('issues')
