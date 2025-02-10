from flask import Flask

app = Flask(__name__)

# ✅ Fix: Add a home route to prevent 404 errors
@app.route("/")  
def home():
    return "Flask API is running on Render!"

# Your existing endpoints
@app.route("/receive-data", methods=["POST"])
def receive_data():
    return {"message": "Data received successfully"}

if __name__ == "__main__":
    app.run(debug=True)
