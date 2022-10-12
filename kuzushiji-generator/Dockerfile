FROM python:3.8

RUN apt-get update

RUN mkdir /code
COPY code /code/
WORKDIR /code
RUN pip install -r requirements.txt