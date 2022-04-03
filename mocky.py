from flask import Flask


### Import Blue Prints ###
#Import IP Info Blue Print
from integrations.ipinfo.ipinfo import ipinfo_bp 
from integrations.tufin.tufin import tufin_bp 

app = Flask(__name__)

## Put the App into Debug mode
app.config["DEBUG"] = True


#Register Vedor Simulation IP Info
app.register_blueprint(ipinfo_bp)
app.register_blueprint(tufin_bp)

app.run(host="0.0.0.0", port=5000, ssl_context='adhoc')
