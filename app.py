from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route for the root URL
@app.route("/")
def home():
    return "Welcome to Flask Cloud App!"

# Define the compute_sum endpoint
@app.route("/compute_sum", methods=["POST"])
def compute_sum():
    data = request.get_json()
    numbers = data.get("numbers", [])
    result = sum(numbers)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

