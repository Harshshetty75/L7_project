# L7_project

# Chocolate House Management System

This is a simple Python application for a fictional chocolate house that manages seasonal flavor offerings, ingredient inventory, and customer flavor suggestions along with allergy concerns. The application uses Flask as a web framework and SQLite as the database.

## Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- SQLite

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Harshshetty75/L7_project.git
   cd your-repo-name
   ```

2. **Install Python Dependencies**
   Make sure you have Python 3.10 or higher installed. Install the required packages by running:
   ```bash
   pip install flask
   pip install flask-sqlalchemy
   ```

## Running the Application

1. **Start the Flask Application**
   Navigate to the project directory where `app.py` is located, and run:
   ```bash
   python app.py
   ```

2. **Access the Application**
   Open your web browser and go to [http://localhost:5000](http://localhost:5000) to use the application.


   ## Build and Run the Application Using Docker

To run this application using Docker, follow these steps:

1. **Build the Docker Image**  
   Open your terminal or command prompt and navigate to the project directory where the Dockerfile is located. Run the following command to build the Docker image:

   ```bash
   docker build -t chocolate-house-app .
   ```

2. **Run the Docker Container**  
   After the image has been built successfully, run the Docker container using the following command:

   ```bash
   docker run -p 5000:5000 chocolate-house-app
   ```

   This command maps port 5000 on your local machine to port 5000 in the Docker container.

3. **Access the Application**  
   Once the container is running, open your web browser and navigate to:

   ```arduino
   http://localhost:5000
   ```

   This will allow you to access the application running inside the Docker container.

4. **Stop the Application**  
   To stop the application, return to the terminal where the Docker container is running and press `CTRL+C`. If you want to remove the container, you can use the following command after stopping it:

   ```bash
   docker ps -a  # to list all containers
   docker rm <container_id>  # replace <container_id> with the actual ID of the stopped container
   ```

Make sure Docker is installed and running on your machine before executing these commands.


---



