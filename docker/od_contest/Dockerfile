FROM python:3.13-slim

# Ensure logs are shown immediately
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Config for project
ENV ENVIRONMENT=docker

WORKDIR /src
