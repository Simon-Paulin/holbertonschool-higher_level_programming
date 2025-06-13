#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
    }

@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"

@app.route("/data")
def data():
   
    return jsonify(users)

@app.route("/status")
def status():
    return "<p>OK</p>"

@app.route("/users/<username>")
def users_list(username):
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])
def add_user():
    if request.method == "POST":
        return jsonify(users["john"])

if __name__ == "__main__":
    app.run(debug=True)
