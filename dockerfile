FROM python:2.7

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

ADD . /flask-server
WORKDIR /flask-server
RUN pip install -r requirements.txt