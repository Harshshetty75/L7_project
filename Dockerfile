# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install the required packages with specific versions to ensure compatibility
RUN pip install --no-cache-dir flask==2.1.3 flask-sqlalchemy==2.5.1 "SQLAlchemy<2.0" "Werkzeug==2.0.3"

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
