from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/receive-data", methods=["POST"])
def receive_data():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data received"}), 400

        
        print("Received Data:", data)

        
        processed_data = process_data(data)

        
        return jsonify({"message": "Data received successfully", "processed_data": processed_data}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def process_data(data):
    """
    Function to process and clean data (Modify this as needed)
    """
    
    return data

if __name__ == "__main__":
    app.run(debug=True, port=5000)
