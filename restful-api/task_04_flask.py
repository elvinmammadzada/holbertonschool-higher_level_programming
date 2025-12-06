#!/usr/bin/python3
"""Web app with flask"""
from flask import Flask
from flask import jsonify
from flask import request

users = {}
user_error = {"error": "User not found"}
user_exist = {"error":"Username already exists"}
user_req = {"error":"Username is required"}
invalid_json = {"error":"Invalid JSON"}

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"
@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)
@app.route("/status")
def status():
    return "OK"
@app.route("/users/<username>")
def userws(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify(user_error), 404
@app.route("/add_user", methods = ["POST"])
def add_user():
    new_user = request.get_json(silent=True)
    if new_user is None:
        return jsonify(invalid_json), 400
    username = new_user.get("username")
    if not username:
        return jsonify(user_req), 400
    if username in users:
        return jsonify(user_exist), 409
    users[username] = new_user
    return jsonify({"message": "User added", "user" : new_user}), 201

if __name__ == "__main__":
    app.run()
