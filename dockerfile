FROM ubuntu:latest
MAINTAINER Jithin Thomas "thomasjtt.2@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
ENV HOME=/app
WORKDIR /app

RUN pip install -r requirements.txt


EXPOSE 5000

ENTRYPOINT ["python"]
CMD [app.py]
