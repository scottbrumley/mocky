from flask import Blueprint
from flask import Response
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

INTEGRATION = "panorama"

# Hard Code User and Password
user = 'palo01'
pw = 'palo01'

# Panorama Root URLs
API_KEY = "7777777"
panorama_url = "/panorama"


auth = HTTPBasicAuth()
panorama_bp = Blueprint(f"{INTEGRATION}" + '_bp', __name__)

users = {
    user: generate_password_hash(pw)
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


# Test Link
@panorama_bp.route(panorama_url, methods=['GET'])
@auth.login_required
def panorama_test():
    xml = 'foo'
    return Response(xml, mimetype='text/xml')
