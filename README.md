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
2. Ensure evnironment variables are set by running `echo $<ENVAR>`
3. Call boot.sh by running `./boot.sh` from project root directory
4. *In a new terminal* Call css load by running `npm start` from the static directory

## How to Close

1. On both terminals run OPTION-C
2. To confirm reload page and ensure is down

## Todo
V2.0
Dyanmic Resume download
Index elements in database

Questions for max
need resume for download button


AS OF 9/7/20 - REVEIW WITH MAX
Sticky footer
ticker on hover scroll stops 
show tags and collabs already in use on update page

COMPELTED -- collaborators field on right side = project details - link to github profiles little avatar or their name like discord TP in circle
COMPLETED -- click email copies to clipboard - footer
COMPLETED -- open link to new tabs not current
COMPLETED -- sticky footer
COMPLETED -- ticker links to tag detail page 
COMPLETED -- padding to index picture at small resolution
COMPLETED -- space under principal engineer needs to be fixed - centered
COMPLETED -- signify featured on projects page 
COMPLETED -- limit featured projects to three per row
COMPLETED -- link to pages on education/experience
COMPLETED -- footer: linked in icon

PROJECT PAGE
COMPLETED -- don't like blocks of green - less green
COMPLETED -- tags under title
COMPLETED -- place link elsewhere - with a standard link icon

PROJECT DESCRIPTION:
COMPLETED -- no green hero 
COMPELTED -- project link with icon // do both to see icon looks weird

TAG DETAIL:
COMPLETED -- same as project list no green

Project CRUD:
editor with text - bold, underlineable, etc  wysiwyg editor
----
AS OF 9/2/20
COMPLETED -- Need twitter profile link
COMPLETED -- any other links in footer
COMPLETED -- Login to view CRUD menus
COMPLETED -- .textarea updates - spacing and vertical align
COMPELTED -- Logo
COMPLETED -- Updated Picture
COMPLETED -- tag page - create it
COMPLETED -- links need to be actual links around page for external sites - project pages 

----
single page to show topics 
expand aspects to different page

brief description with a ...read more to a deeper page 

technologies used to complete projects

travis: travis, dev ops
cloud: kubernetes, docker
Nex: web development, python, flask
lets talk: education, mentoring
Talos: web development, PHP

## TO START

Execute 'FLASK_APP=flask_app.py' in terminal
Execute './boot.sh'

