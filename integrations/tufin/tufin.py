from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from integrations.tufin.dataset import applications_info, devices_info, app_connections_info



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

    def get_ents(self, group, entity, search_dict):
        ents = {}

        if entity and group:
            ents[group] = {}
            ents[group][entity] = []
        else:
            return ents

        ttlCount = 0
        findEnts = []
        # Look through each entity in the entities group
        for entity_item in self.ents[group][entity]:
            ttlCount = ttlCount + 1
            if search_dict:
                params_found = True
                key_found = True
                # look through the values in the entity
                for key, value in entity_item.items():
                    key_found = True
                    # Find all values that were in the parameters
                    for requests_key, requests_value in search_dict.items():
                        if requests_key == "id" or requests_key == "applicationId":
                            requests_value = int(requests_value)

                        # If the Key is not Found in the data source then do not return
                        if requests_key not in entity_item:
                            key_found = False
                            pass
                        # If Key and value matches then continue
                        if key == requests_key and value == requests_value:
                            continue
                        else:
                            # If the value of the key is not equal then parameter was not found
                            if key == requests_key and value != requests_value:
                                params_found = False
                if params_found and key_found:
                    findEnts.append(entity_item)
                else:
                    continue
            else:
                # Get all entities when no parameters are given
                findEnts.append(entity_item)

        ents[group]['count'] = len(findEnts)
        ents[group]['total'] = ttlCount
        ents[group][entity] = findEnts
        return ents


def harvest_args(arg_dict):
    returnDict = {}
    for key, val in arg_dict.items():
        returnDict[key] = val
    return returnDict


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
    args = request.args
    devices = QueryEntity(devices_info)
    devices_dict = devices.get_ents('devices', 'device', args)
    return jsonify(devices_dict)


# Secure Change Workflow Applications 
@tufin_bp.route(secureworkflow + '/secureapp/repository/applications', methods=['GET'])
@auth.login_required
def securechangeworkflow_apps_all():
    args = request.args
    applications = QueryEntity(applications_info)
    applications_dict = applications.get_ents('applications', 'application', args)
    return jsonify(applications_dict)

# Secure Applications Connections
@tufin_bp.route(secureworkflow + '/secureapp/repository/applications/<appid>/connections', methods=['GET'])
@auth.login_required
def secureapp_connections(appid):
    args = request.args
    print(appid, flush=True)
    print(args, flush=True)
    my_args = harvest_args(args)
    my_args['applicationId'] = int(appid)
    connections = QueryEntity(app_connections_info)
    connections_dict = connections.get_ents('connections', 'connection', my_args)
    return jsonify(connections_dict)
