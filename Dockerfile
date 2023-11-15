FROM python:3.7-slim-buster

LABEL Author="Sneha Gaddam"

# Python variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /src
WORKDIR /src

RUN apt-get update
COPY requirements.txt /src/requirements.txt

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r ./requirements.txt

# Install src
COPY src /src
