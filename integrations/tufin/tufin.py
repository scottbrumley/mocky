from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


auth = HTTPBasicAuth()
tufin_bp = Blueprint('tufin_bp', __name__)

# Hard Code User and Password
user = 'tufin'
pw = 'tufin'

# TuFin Root URLs
secureworkflow = "/securechangeworkflow/api"
securetrack = "/securetrack/api"

users = {
    user: generate_password_hash(pw)
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@tufin_bp.route(secureworkflow + '/securechange/devices', methods=['GET'])
@auth.login_required
def securechangeworkflow_all():
    devices_info = {
        "devices":
               {"device": [   
                               {
                               "id": 553,
                               "name": request.args.get('name'),
                               "ip": "9.9.9.9",
                               "vendor": "Cisco",
                               "device_type": "asa"
                               },
                               {
                               "id": 2,
                               "name": "cisco_device_name",
                               "ip": "7.7.7.7",
                               "vendor": "Cisco",
                               "device_type": "router"
                               }
                          ]
                }

    }
    return jsonify(devices_info)


# SecureTrack Devices
@tufin_bp.route(securetrack + '/devices', methods=['GET'])
@auth.login_required
def securetrack_all():
    devices_info = {
        "devices":
               {
                "count": 2,
                "total": 5000,
                "device": [   
                               {
                               "id": 553,
                               "name": request.args.get('name'),
                               "ip": "9.9.9.9",
                               "model": "5520",
                               "vendor": "Cisco",
                               "device_type": "asa"
                               },
                               {
                               "id": 2,
                               "name": "cisco_device_name",
                               "ip": "7.7.7.7",
                               "model": "2930",
                               "vendor": "Cisco",
                               "device_type": "router"
                               }
                          ]
                }

    }
    return jsonify(devices_info)


# Secure Change Workflow Applications 
@tufin_bp.route(secureworkflow + '/secureapp/repository/applications', methods=['GET'])
@auth.login_required
def securechangeworkflow_apps_all():
    info = {
        "applications":
               {
                "application": [   
                               {
                               "id": "443",
                               "name": request.args.get('name'),
                               "vendor": "Service Now",
                               "comment": "",
                               "owner": {
                                         "name": "Jack Reacher",
                                         "id": "2"
                               },
                               "status": "CONNECTED",
                               "decommissioned": False
                               },
                               {
                               "id": "3",
                               "name": "Jira",
                               "vendor": "Atlassian",
                               "comment": "",
                               "owner": {
                                         "name": "John Wick",
                                         "id": "3"
                               },
                               "status": "CONNECTED",
                               "decommissioned": False
                               }
                          ]
                }

    }
    return jsonify(info)
