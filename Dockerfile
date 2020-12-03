FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive


ENV FLASK_APP flask_app.py
ENV FLASK_CONFIG production

RUN apt-get update
RUN apt-get install -y python3-dev python3 libjpeg-dev zlib1g-dev pkg-config graphviz graphviz-dev gcc musl-dev nodejs npm wkhtmltopdfpu tzdata
ENV LIBRARY_PATH=/lib:/usr/lib


RUN adduser bender
USER bender

WORKDIR /home/bender

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/python -m pip install -U --force-reinstall pip
RUN venv/bin/pip install wheel
RUN venv/bin/pip install pygraphviz --install-option="--library-path=/usr/lib/graphviz/"
RUN venv/bin/pip install -r requirements.txt

COPY --chown=bender:bender app app 
COPY --chown=bender:bender migrations migrations
COPY --chown=bender:bender flask_app.py config.py boot.sh ./

WORKDIR /home/bender/app/static/node_modules

RUN npm install

WORKDIR /home/bender

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
