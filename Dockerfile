# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Set environment variables to prevent Python from writing .pyc files
# and to output logs directly to the terminal
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
# This step is done separately to leverage Docker's build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port on which FastAPI will run
EXPOSE 8000

# Define the command to run the FastAPI application with Uvicorn
# Replace 'main:app' with the actual path to your FastAPI application instance
CMD ["uvicorn", "main:demo", "--host", "0.0.0.0", "--port", "8000"]