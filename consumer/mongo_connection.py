from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv
import json
load_dotenv()



mongo_uri = getenv("MONGODB_URL", "mongodb://mongo:27017")
mongo_db = getenv("DATABASE_NAME", "border-cameras")
mongo_collection = getenv("MONGO_COLLECTION", "notifications")
file_path = '.data/border_alerts.json'

def mongo_conn():
    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    notifications_col = db[mongo_collection]

    with open(file_path) as file:
        file_data = json.load(file)
    ins_result = notifications_col.insert_many(file_data)
    print(f"Data inserted to MongoDB. Documents inserted: {len(ins_result.inserted_ids)}")
    return notifications_col
    
    

