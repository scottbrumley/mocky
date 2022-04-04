from flask import make_response
from flask import Blueprint
from integrations.palo_alto_networks.panorama.dataset import testing

INTEGRATION = "panorama"

# Panorama Root URLs
API_KEY = "7777777"
panorama_url = "/" + INTEGRATION

panorama_bp = Blueprint(f"{INTEGRATION}" + '_bp', __name__)

# Test Link
@panorama_bp.route(panorama_url + "/api", methods=['GET'])
def panorama_test():
    xml = "<body>test</body>"
    response = make_response(testing)
    response.headers['Content-Type'] = 'text/xml; charset=utf-8'
    return response
