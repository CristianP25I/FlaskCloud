import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Cloud App!"

@app.route("/compute_sum", methods=["POST"])
def compute_sum():
    data = request.get_json()
    numbers = data.get("numbers", [])
    result = sum(numbers)
    return jsonify({"result": result})

if __name__ == "__main__":
    # Use Render's dynamic port, default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


