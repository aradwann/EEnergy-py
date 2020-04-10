# Dockerfile

# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /code/
RUN pipenv install --system

# Setup GDAL
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal

# Copy project
COPY . /code/
