from flask import make_response
from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from integrations.palo_alto_networks.panorama.dataset import testing

INTEGRATION = "panorama"

# Hard Code User and Password
user = 'palo01'
pw = 'palo01'

# Panorama Root URLs
API_KEY = "7777777"
panorama_url = "/" + INTEGRATION


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
@panorama_bp.route(panorama_url + "/api", methods=['GET'])
@auth.login_required
def panorama_test():
    xml = "<body>test</body>"
    response = make_response(testing)
    response.headers['Content-Type'] = 'text/xml; charset=utf-8'
    return response
