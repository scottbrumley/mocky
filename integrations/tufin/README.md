# TuFin Integration


## Documentation:
* [TOS Knowledge Center](https://forum.tufin.com/support/kc/latest/Content/Suite/4423.htm?tocpath=The%20TOS%20Developers%20Guide%7CThe%20TOS%20REST%20API%7CGetting%20Started%20with%20the%20TOS%20API%7C_____0)
* [SecureTrack Swagger](https://forum.tufin.com/support/kc/rest-api/R21-3/securetrack/apidoc/#!/Monitored_Devices/getDevices)
* [Secure Change Work Flow](https://forum.tufin.com/support/kc/rest-api/R21-3/securechangeworkflow/apidoc/#!/Applications/getApplications)

# Building Docker Container
Run "./build.sh" for Production and "./build.sh dev" for Development.
The dev option will build with testing packages and the container will have -dev appended to the name.

# Running Docker Container
Run "./start.sh" for Production and "./start.sh dev" for Development.

## Testing
To Run Unit Test use: "python -m pytest" outside the docker container.  Insure you're enviroment has requirements from requirements-dev.txt such as pytest.


# Stopping Docker Container
Run "./stop.sh" for Production and "./stop.sh dev" for Development

