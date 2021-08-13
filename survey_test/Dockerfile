FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /survey_test

COPY ./rq.txt /rq.txt
RUN pip install -r /rq.txt

COPY . /survey_test
