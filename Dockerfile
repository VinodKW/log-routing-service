# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Create and activate the virtual environment
RUN python3 -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . .
