from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash


class QueryEntity:
    """
    Examples of Entities in Dictionary
        ents = {
            "devices":
                {"device": [
                ]
                }
        }
        """
    def __init__(self, dictParam):
        self.ents = dictParam

    def get_ents(self, group, entity, searchterm):
        ents = {}

        if entity and group:
            ents[group] = {}
            ents[group][entity] = []
        else:
            return ents

        ttlCount = 0
        findEnts = []
        for device in self.ents[group][entity]:
            ttlCount = ttlCount + 1

            if searchterm:
                for key, value in device.items():
                    if key == 'name' and value == searchterm:
                        findEnts.append(device)
            else:
                findEnts.append(device)

        ents[group]['count'] = len(findEnts)
        ents[group]['total'] = ttlCount
        ents[group][entity] = findEnts

        return ents


auth = HTTPBasicAuth()
tufin_bp = Blueprint('tufin_bp', __name__)

# Hard Code User and Password
user = 'tufin'
pw = 'tufin'

# TuFin Root URLs
secureworkflow = "/securechangeworkflow/api"
securetrack = "/securetrack/api"

# Dictionaries of Responses 
devices_info = {
    "devices":
        {
            "device": [
                {
                    "id": 553,
                    "name": "asa",
                    "ip": "9.9.9.9",
                    "model": "5520",
                    "vendor": "Cisco",
                    "device_type": "asa"
                },
                {
                    "id": 2,
                    "name": "cisco_device_name",
                    "ip": "7.7.7.7",
                    "model": "2940",
                    "vendor": "Cisco",
                    "device_type": "router"
                }
            ]
        }
}

users = {
    user: generate_password_hash(pw)
}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


# SecureTrack Devices
@tufin_bp.route(securetrack + '/devices', methods=['GET'])
@auth.login_required
def securetrack_all():
    name = request.args.get('name')
    devices = QueryEntity(devices_info)
    devices_dict = devices.get_ents('devices', 'device', name)

    return jsonify(devices_dict)


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
