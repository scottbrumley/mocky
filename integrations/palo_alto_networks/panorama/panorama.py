from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


auth = HTTPBasicAuth()
palo_panorama_bp = Blueprint('palo_panorama_bp', __name__)

# Hard Code User and Password
user = 'palo01'
pw = 'palo01'

# Panorama Root URLs
PORT = "443"
API_KEY = "7777777"
URL = "/securechangeworkflow:" + PORT + "/api"

users = {
    user: generate_password_hash(pw)
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

