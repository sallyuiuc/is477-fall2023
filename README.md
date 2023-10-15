# is477-fall2023
# Lab 1 redux title 

A NEW REPRODUCING SECTION
step1: git clone https://github.com/sallyuiuc/is477-fall2023

step2:  FROM python:3.7
        COPY. /app
        WORKDIR /app
        RUN pip install -r requirements.txt
        CMD python main.py

step3:

docker build -t image-name .
docker run image-name
