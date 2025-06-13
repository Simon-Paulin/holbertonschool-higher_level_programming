#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
    }

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
        return "User not found", 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return "Username is required", 400
    if username in users:
        return "Username already exists", 400
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify(users[username]), 201

if __name__ == "__main__":
    app.run()
