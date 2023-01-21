FROM python:3.8

RUN pip install uwsgi
RUN mkdir /var/log/uwsgi/
ADD django.ini /etc/uwsgi/django.ini
ADD django.conf /etc/nginx/sites-available/django.conf

WORKDIR /E-Commerce-Backend-Django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip

COPY . .

RUN apt-get update
RUN apt-get install bash
RUN apt-get install -y nginx
RUN ln -s /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled/django.conf
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

EXPOSE 8000
