FROM python:3.8-alpine

ENV FLASK_APP flask_app.py
ENV FLASK_CONFIG production

RUN apk add build-base python3-dev py-pip jpeg-dev zlib-dev pkgconfig graphviz graphviz-dev gcc musl-dev nodejs npm wkhtmltopdf
ENV LIBRARY_PATH=/lib:/usr/lib

RUN adduser -D bender
USER bender

WORKDIR /home/bender

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/python -m pip install -U --force-reinstall pip
RUN venv/bin/pip install wheel
RUN venv/bin/pip install pygraphviz --install-option="--library-path=/usr/lib/graphviz/"
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY flask_app.py config.py boot.sh ./

RUN chown -R bender:bender /home/bender

WORKDIR /home/bender/app/static/node_modules

RUN npm install

WORKDIR /home/bender

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
