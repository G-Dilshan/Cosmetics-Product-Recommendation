# Use Python 3.12 base image
FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-jdk \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /flask-app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application
COPY . .

# Create necessary directories
RUN mkdir -p /flask-app/uploads /flask-app/generated /flask-app/temp

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=production
ENV MAX_CONTENT_LENGTH=16777216
ENV UPLOAD_FOLDER=/flask-app/uploads
ENV GENERATED_FOLDER=/flask-app/generated

# Expose port 5000
EXPOSE 5000

# Command to run the application with Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "main:app"]