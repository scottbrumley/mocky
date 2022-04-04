from flask import make_response
from flask import Blueprint
from flask import request
from integrations.palo_alto_networks.panorama.dataset import system_info

INTEGRATION = "panorama"

# Panorama Root URLs
API_KEY = "7777777"
panorama_url = "/" + INTEGRATION

panorama_bp = Blueprint(f"{INTEGRATION}" + '_bp', __name__)


class Commands:
    def __init__(self):
        return

    def run_command(self,exec_cmd, cmd_type):
        return_value = "<xml>No Value</xml>"
        if exec_cmd and cmd_type:
            return_value = system_info
        return return_value


# Test Link
@panorama_bp.route(panorama_url + "/api/", methods=['GET'])
def panorama_test():
    param_key = request.args.get("key")
    param_type = request.args.get("type")
    param_cmd = request.args.get("cmd")
    print(param_cmd, flush=True)
    if param_key == API_KEY:
        exec_cmds = Commands()
        ret_response = exec_cmds.run_command(param_cmd, param_type)
        response = make_response(ret_response)
    else:
        msg = "<xml>API KEY Not Correct</xml>"
        response = make_response(msg)
    response.headers['Content-Type'] = 'text/xml; charset=utf-8'
    return response
