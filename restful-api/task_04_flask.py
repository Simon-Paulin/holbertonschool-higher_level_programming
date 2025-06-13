#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(users)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def users_list(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify(users[username]), 201

if __name__ == "__main__":
    app.run()
