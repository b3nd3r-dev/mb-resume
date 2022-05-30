FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
ENV LIBRARY_PATH=/lib:/usr/lib

RUN apt-get update
RUN apt-get install -y python3-dev python3 libjpeg-dev zlib1g-dev pkg-config gcc musl-dev nodejs npm wkhtmltopdf tzdata python3-venv python3-pip
RUN apt-get install -y vim

RUN adduser bender
USER bender

WORKDIR /home/bender

COPY --chown=bender:bender app app 
COPY --chown=bender:bender migrations migrations
COPY --chown=bender:bender flask_app.py config.py boot.sh ./

WORKDIR /home/bender/app/static

RUN npm install

WORKDIR /home/bender

COPY requirements.txt requirements.txt
RUN python3 -m venv venv
RUN venv/bin/python -m pip install -U --force-reinstall pip
RUN venv/bin/pip install wheel
RUN venv/bin/pip install -r requirements.txt

ENV FLASK_APP=/home/bender/flask_app.py
ENV FLASK_CONFIG=development

# run-time configuration
EXPOSE 5001
ENTRYPOINT ["./boot.sh"]
