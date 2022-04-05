from flask import Blueprint
from flask import jsonify


INTEGRATION = "ipinfo"

ipinfo_bp = Blueprint(f"{INTEGRATION}" + '_bp', __name__)


@ipinfo_bp.route("/" + INTEGRATION + '/<ip>/json', methods=['GET'])
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
        "readme": "https://ipinfo.io/missingauth",
        "region": "California",
        "timezone": "America/Los_Angeles"
    }
    return jsonify(ip_info)
