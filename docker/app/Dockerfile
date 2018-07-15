FROM ubuntu:latest

MAINTAINER Yuta Oikawa

RUN apt-get upgrade -y && apt-get update -y
RUN apt-get install -y \
    wget \
    curl \
    git \
    zsh \
    vim \
    tree \
    gcc \
    make \
    openssl \
    zlib1g-dev \
    libssl-dev \
    libbz2-dev \
    libreadline-dev \
    language-pack-ja-base \
    language-pack-ja \
    ibus-mozc \
    build-essential \
    python3-dev \
    python3-pip \
    zip \
    unzip

RUN update-locale LANG=ja_JP.UTF-8 LANGUAGE=ja_JP:ja
ENV LANG ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8

RUN pip3 install --upgrade pip
RUN pip3 install \
    setuptools \
    flask \
    uwsgi
#RUN pip3 install \
#    setuptools \
#    cupy-cuda92 \
#    cupy \
#    chainer \
#    scipy \
#    pandas \
#    scikit-learn \
#    pillow \
#    h5py \
#    --no-cache-dir

RUN mkdir workspace

#WORKDIR /workspace/app

CMD ["uwsgi","--ini","/workspace/app/uwsgi.ini"]
