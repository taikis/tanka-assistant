FROM python:3.8

RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN mkdir /code
COPY code /code/
WORKDIR /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt