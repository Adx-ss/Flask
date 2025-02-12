import os
from pymongo import MongoClient

# ✅ Fetch MongoDB URI from Render's environment variables
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["Sample"]  # Database name
collection = db["your_collection_name"]  # Replace with actual collection
