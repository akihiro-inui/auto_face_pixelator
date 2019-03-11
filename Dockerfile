FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    python3 \
    python3-pip
RUN pip3 install --upgrade pip==19.0.3 \
    && pip3 install setuptools

RUN brew install cmake

RUN brew install boost-python

RUN conda install -c menpo dlib=18.18

# for flask web server
#EXPOSE 8081

# set working directory
#ADD . /app
#WORKDIR /app

# install required libraries
RUN pip3 install -r requirements.txt

# This is the runtime command for the container
#CMD python3 app.py
