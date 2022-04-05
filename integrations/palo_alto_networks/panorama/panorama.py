import re
from flask import make_response
from flask import Blueprint
from flask import request
from integrations.palo_alto_networks.panorama.dataset import *

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
        if exec_cmd == "<show><system><info></info></system></show>" and cmd_type == "op":
            return_value = system_info
        if re.search("<show><jobs><id>(.*)</id></jobs></show>", exec_cmd) and cmd_type == "op":
            my_id = re.search("<show><jobs><id>(.*)</id></jobs></show>", exec_cmd).group(1)
            return_value = jobs_id(my_id)
        if "<request><content><upgrade><download><latest/>" in exec_cmd and cmd_type == "op":
            return_value = download_content_upgrade
        if "<request><content><upgrade><install><version>latest</version></install></upgrade></content></request>" \
                and cmd_type == "op":
            return_value = install_content_upgrade
        return return_value


# Test Link
@panorama_bp.route(panorama_url + "/api/", methods=['POST', 'GET'])
def panorama_test():

    print(request.method, flush=True)
    if request.method == "POST":
        param_key = request.form["key"]
        param_type = request.form["type"]
        param_cmd = request.form["cmd"]

    else:
        param_key = request.args.get("key")
        param_type = request.args.get("type")
        param_cmd = request.args.get("cmd")

    if param_key == API_KEY:
        exec_cmds = Commands()
        ret_response = exec_cmds.run_command(param_cmd, param_type)
        response = make_response(ret_response)
    else:
        msg = "<xml>API KEY Not Correct</xml>"
        response = make_response(msg)
    response.headers['Content-Type'] = 'text/xml; charset=utf-8'
    return response
