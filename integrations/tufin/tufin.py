from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from integrations.tufin.dataset import applications_info,devices_info



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
    name = request.args.get('name')
    applications = QueryEntity(applications_info)
    applications_dict = applications.get_ents('applications', 'application', name)
    return jsonify(applications_dict)
