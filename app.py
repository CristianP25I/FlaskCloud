import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Cloud App!"

# Endpoint for temperature data
@app.route("/temperature", methods=["POST"])
def temperature():
    data = request.get_json()
    temperature = data.get("temperature")
    timestamp = data.get("timestamp")
    if temperature and timestamp:
        print(f"Received temperature: {temperature}°C at {timestamp}")
        return jsonify({"message": "Temperature data received"}), 200
    else:
        return jsonify({"error": "Invalid data format"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render's dynamic port, default to 5000 locally
    app.run(host="0.0.0.0", port=port)


