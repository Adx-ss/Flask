import os
from flask import Flask, request, jsonify
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

@app.route("/query-mongo-data", methods=["GET"])
def query_mongo_data():
    """
    Fetch MongoDB data and allow filtering by accountId or primary_media_buyer.
    """
    try:
        # Get query parameters
        account_id = request.args.get("accountId")
        media_buyer = request.args.get("primary_media_buyer")

        # Build the query dynamically
        query = {}
        if account_id:
            query["acountId"] = account_id  # Keep original MongoDB field name
        if media_buyer:
            query["primary_media_buyer"] = media_buyer

        # Fetch data from MongoDB
        data = list(collection.find(query, {"_id": 0}))  # Exclude `_id`
        
        return jsonify({"message": "Data retrieved", "data": data})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Ensure Gunicorn can find "app"
if __name__ == "__main__":
    app.run(debug=True)
