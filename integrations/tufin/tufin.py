from flask import Blueprint
from flask import request, jsonify


tufin_bp = Blueprint('tufin_bp', __name__)


@tufin_bp.route('/securechangeworkflow/api/secureapp/repository/applications/{}/connections/<app_id>', methods=['GET'])
def api_all(ip):
    ip_info = {
        "anycast": True,
        "city": "Los Angeles",
        "country": "US",
        "hostname": "one.one.one.one",
        "ip": ip,
        "lat": 34.0522,
        "lng": -118.2437,
        "loc": "34.0522,-118.2437",
        "org": "AS13335 Cloudflare, Inc.",
        "postal": "90084",
        "readme": "https://tufin.io/missingauth",
        "region": "California",
        "timezone": "America/Los_Angeles"
    }
    return jsonify(ip_info)
