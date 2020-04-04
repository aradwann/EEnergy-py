# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /EEnergy

# Install dependencies
COPY Pipfile Pipfile.lock /EEnergy/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /EEnergy/