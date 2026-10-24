#!/usr/bin/python3
"""Create a simple API using Flask."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users are stored in memory.
users = {}


@app.route("/", methods=["GET"])
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def get_users():
    """Return a list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return the details of a specific user."""
    user = users.get(username)

    if user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user), 200


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the API."""
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if not isinstance(username, str):
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()