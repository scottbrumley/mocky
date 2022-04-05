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
        if exec_cmd == "<show><system><info></info></system></show>" and cmd_type == "op":
            return_value = system_info
        elif re.search("<show><jobs><id>(.*)</id></jobs></show>", exec_cmd) and cmd_type == "op":
            my_id = re.search("<show><jobs><id>(.*)</id></jobs></show>", exec_cmd).group(1)
            return_value = jobs_id(my_id)
        elif "<request><content><upgrade><download><latest/>" in exec_cmd and cmd_type == "op":
            return_value = download_content_upgrade
        elif "<request><content><upgrade><install><version>latest</version></install></upgrade></content></request>" \
                and cmd_type == "op":
            return_value = install_content_upgrade
        elif "<request><system><software><check>" in exec_cmd and cmd_type == "op":
            return_value = pan_os_upgrade_check
        elif "<request><system><software><download>" in exec_cmd and cmd_type == "op":
            return_value = pan_os_upgrade_install
        elif "<request><restart><system>" in exec_cmd and cmd_type == "op":
            return_value = restart_fw
        elif "<test><security-policy-match>" in exec_cmd and cmd_type == "op":
            return_value = test_security_policy
        #elif "<show><objects>" in exec_cmd:
        #    return_value showobjects(command)
        elif "<test><url-info-host>" in exec_cmd:
            my_host = re.search("<test><url-info-host>(.*)</url-info-host></test>", exec_cmd).group(1)
            return_value = get_url_info_from_host(my_host)
        elif "<test><url-info-cloud>" in exec_cmd:
            my_host = re.search("<test><url-info-cloud>(.*)</url-info-cloud></test>", exec_cmd).group(1)
            return_value = get_url_info_from_cloud(my_host)
        elif "<test><url>" in exec_cmd:
            my_url = re.search("<test><url>(.*)</url></test>", exec_cmd).group(1)
            return_value = test_url(my_url)
        elif "<request><plugins><cloud_services>" in exec_cmd:
            return_value = prisma_access_logout(exec_cmd)
        else:
            return_value = system_info
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
