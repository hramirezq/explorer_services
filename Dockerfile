# Base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y netcat

# Set the working directory
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/explorer_services_api

# Copy requirements and install dependencies
COPY .pip_cache /opt/app/pip_cache/
COPY requirements.txt /opt/app/
COPY explorer_services_api /opt/app/explorer_services_api/
COPY tests /opt/app/tests/
COPY manage.py /opt/app/

WORKDIR /opt/app
RUN python -m venv env
RUN python -m pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# Start the application
CMD python manage.py runserver 0.0.0.0:8000

