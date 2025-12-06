#!/usr/bin/python3
"""Template with Jinja"""
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def item():
    try:
        with open("items.json", "r") as file:
            json_file = json.load(file)
            if isinstance(json_file, dict):
                items = json_file.get("items", [])
            elif isinstance(json_file, list):
                items = json_file
            else:
                items = []
    except (FileNotFoundError, json.JSONDecodeError):
        items = []
    return render_template('items.html', items=items)
if __name__ == '__main__':
    app.run(debug=True, port=5000)
