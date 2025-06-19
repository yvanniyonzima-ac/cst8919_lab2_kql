from flask import Flask, request, jsonify
import logging
import os
from datetime import datetime

app = Flask(__name__)

# Configure logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'login_attempts.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Dummy credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "secret"

@app.route('/')
def index():
    return "Welcome to the Flask Login App!"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        logging.info(f"SUCCESSFUL login attempt by user: {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        logging.warning(f"FAILED login attempt by user: {username}")
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)
