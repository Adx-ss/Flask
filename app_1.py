import os
from flask import Flask, jsonify
from pymongo import MongoClient

# ✅ Initialize Flask App
app = Flask(__name__)  # ✅ Make sure the instance is named "app"

# ✅ Fetch MongoDB URI from Render's environment variables
MONGO_URI = os.getenv("MONGO_URI")

# ✅ Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client["Sample"]  # Database name
collection = db["your_collection_name"]  # Replace with actual collection

@app.route("/")
def home():
    return "Flask API is running on Render!"

@app.route("/get-mongo-data", methods=["GET"])
def get_mongo_data():
    """
    Retrieve data from MongoDB and return as JSON.
    """
    try:
        data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB `_id` field
        return jsonify({"message": "Data retrieved", "data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Ensure Gunicorn can find "app"
if __name__ == "__main__":
    app.run(debug=True)
