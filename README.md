# mb-resume
Max Bender's Online Website Resume

## Pre-Requisites

The mb-resume website is written in Flask which is a web framework written in Python. This was developed on Python 3.7.8 so one way or another... install python 3.7.8!

There is a package required to generate ERD diagarams automatically. If you want this then you will need to install graphviz before installing your python requirements. See [GraphViz](http://graphviz.org/download/) for instructions on how to install. *THEN* if you want to generate ERDs run `pip install -r requirements-dev.txt`

Next create a virtual environment by running `python3 -m venv venv` inside the root directory for this project. Then install the project's dependencies by running `pip install -r requirements.txt`.

Navigate to app/static then run npm install 

## Environment Variables
You have to set some environment variables by using `export ENVAR=VALUE` or creating a file with the variables in it, then `source environment_file.env` before running. 
<!-- See the [Dockerfile](Dockerfile) for an example.  -->

1. FLASK_APP=flask_app.py
<!-- 2. FLASK_CONFIG=development/production -->

## How to Start

1. Ensure no gunicorn processes are running by running `ps aux | grep python | grep gunicorn` then kill any remaining processes by running `sudo kill <PID>` 
2. Ensure evnironment variables are set by running `echo $<ENVAR>`, or set environment variables (see above)
3. Call boot.sh by running `./boot.sh` from project root directory
4. *In a new terminal* Call css load by running `npm start` from the static directory

## How to Close

1. On both terminals run OPTION-C
2. To confirm reload page and ensure is down

