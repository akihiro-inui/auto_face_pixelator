FROM python:3.6-slim-stretch

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
    mkdir -p dlib && \
    git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
    cd  dlib/ && \
    python3 setup.py install --yes USE_AVX_INSTRUCTIONS

## install required libraries
COPY requirements.txt /app/requirements.txt
COPY realtime_demo.py /app/realtime_demo.py
COPY image_process.py /app/image_process.py
COPY server.py /app/server.py
COPY api.py /app/api.py
COPY __init__.py /app/__init__.py

#COPY realtime_demo.py /app/realtime_demo.py
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

# This is API
CMD python3 api.py

## This is for web app
#CMD python3 server.py

# Uncomment this line for realtime application
# CMD python3 realtime_demo.py
