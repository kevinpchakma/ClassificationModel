# Set the base image
FROM python:3.10.2

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN apt-get update && apt-get install -y libjpeg-dev
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port number the API will be served on
EXPOSE 5000

# Start the API
CMD ["python", "app.py"]
