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
COPY requirements.txt /auto_face_pixelator/requirements.txt
COPY realtime_demo.py /auto_face_pixelator/realtime_demo.py
COPY image_process.py /auto_face_pixelator/image_process.py
COPY server.py /auto_face_pixelator/server.py
COPY api.py /auto_face_pixelator/api.py
COPY __init__.py /auto_face_pixelator/__init__.py

#COPY realtime_demo.py /app/realtime_demo.py
ADD . /auto_face_pixelator
WORKDIR /auto_face_pixelator
RUN pip3 install -r requirements.txt
COPY . /auto_face_pixelator

# This is API
#CMD python3 api.py

## This is for web app
#CMD python3 server.py

# flaskアプリケーションの起動
ENV FLASK_APP /auto_face_pixelator/server.py
CMD flask run -h 0.0.0.0 -p 8000

