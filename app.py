from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "app": "UMzuzwana Shuttles",
        "status": "online",
        "message": "Welcome to UMzuzwana Shuttles"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/book", methods=["POST"])
def book():
    data = request.get_json(silent=True) or {}

    name = data.get("name")
    pickup = data.get("pickup")
    destination = data.get("destination")
    date = data.get("date")
    time = data.get("time")

    if not all([name, pickup, destination, date, time]):
        return jsonify({
            "success": False,
            "message": "Please provide name, pickup, destination, date and time."
        }), 400

    return jsonify({
        "success": True,
        "message": "Shuttle booking received.",
        "booking": {
            "name": name,
            "pickup": pickup,
            "destination": destination,
            "date": date,
            "time": time
        }
    })


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
