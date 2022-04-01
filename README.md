# XSOAR Mocky
This project builds a docker container that runs a Python Flask server where XSOAR can run API calls.  It mimics vendors for testing. This project uses Blueprints to allow modular based design by vendor.

* **Dockerfile** - How Docker will build the container
* **build.sh** - This script will be build the docker container from the project directorys using the Dockefile
* **mocky.py** - Main Flask Server 
* **requirements.txt** - The Python requirements document for the container build.
* **start.sh** - Start the container locally.  Requires a container in 'docker images' to run.  Usse the build.sh script
* **stop.sh** - Stop the local container and prune Docker.



