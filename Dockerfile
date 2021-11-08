FROM ubuntu:21.04

RUN apt-get -y update && \
    apt-get install -y python3-minimal python3-ipython python3-pytest && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
