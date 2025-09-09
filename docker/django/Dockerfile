FROM python:3-slim

# Ensure logs are shown immediately
ENV PYTHONUNBUFFERED=1

# Install Python dependencies
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
