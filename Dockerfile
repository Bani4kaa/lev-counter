# Use a base image that includes necessary Python dependencies
FROM python:3.12

# Install system dependencies needed for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any Python dependencies
RUN pip install -r requirements.txt  # Adjust according to your setup

# Command to run your Python script
CMD ["python", "dataset.py"]