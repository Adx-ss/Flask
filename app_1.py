from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask API is running on Render!"

@app.route("/receive-data", methods=["POST"])
def receive_data():
    data = request.get_json()
    print("Received Data from Google Apps Script:", data)  # ✅ Logs data in Render
    return jsonify({"message": "Data received successfully", "received_data": data})

if __name__ == "__main__":
    app.run(debug=True)
