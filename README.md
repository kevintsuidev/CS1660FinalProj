# CS1660FinalProj
This is the first project for CS1660. Follow instructions below to get everything setup.
# Setup
1.Pull the github repository onto computer.
2.CD into the directory with the docker-compose.yml file and run "docker-compose up"
3.All the containers should start downloaded the required files to run
4.Once the containers have pulled all the needed information, the gui should be running at localhost:5000. From there you can click any and all of the links to navigated to each program

#Addition Setup for Applications
Spyder: Opens an xterm terminal on startup, type in "spyder" and spyder desktop ide will start running

Jupyter: Needs a password token that is found in the terminal. Look for a command that looks like this: 

To access the notebook, open this file in a browser:
jupyter_1         |         file:///home/jovyan/.local/share/jupyter/runtime/nbserver-8-open.html
jupyter_1         |     Or copy and paste one of these URLs:
jupyter_1         |         http://68df12264cb3:8888/?token=eaf9c7ff53c01ac87e9382c3fb9bd2fdf38730e5f6472df0
jupyter_1         |      or http://127.0.0.1:8888/?token=eaf9c7ff53c01ac87e9382c3fb9bd2fdf38730e5f6472df0

The token is everything after the "="

Orange: password is just "orange"

VScode: password is just password

Spark: To run a specific file, adjust the environment settings to map to the file you want to run, you will see the workers working in the localhost when you do so. You can find the spark commands listed here: https://hub.docker.com/r/bitnami/spark/

Tableau, SAS, Sonarcloud all require an account to be able to log in.

Can see how I run all programs on my github demo video.
