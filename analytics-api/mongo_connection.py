from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

mongo = MongoClient(os.getenv("MONGODB_URL"))
db = mongo[os.getenv("DATABASE_NAME")]
orders_col = db[os.getenv("ORDERS_COL")]

orders_col.create_index("order_id", unique=True)
