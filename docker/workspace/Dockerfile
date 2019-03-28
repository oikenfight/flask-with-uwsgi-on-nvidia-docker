FROM python:3.7.3

MAINTAINER Yuta Oikawa

RUN apt-get upgrade -y && apt-get update -y

RUN apt-get install -y locales && locale-gen ja_JP.UTF-8 && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc

RUN apt-get install -y \
    wget \
    curl \
    git \
    zsh \
    vim \
    tree \
    gcc \
    make \
    openssl

RUN pip install --upgrade pip
RUN pip install \
    setuptools \
    flask \
    uwsgi

RUN mkdir workspace

CMD ["uwsgi","--ini","/workspace/app/uwsgi.ini"]
