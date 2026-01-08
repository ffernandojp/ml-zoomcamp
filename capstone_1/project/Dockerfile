# Lightweight official Python base image
FROM python:3.14-slim

# Install pipenv to manage dependencies
RUN pip install pipenv

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first (for better Docker layer caching)
COPY requirements.txt .

# Install dependencies + verify gunicorn
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn && \
    which gunicorn

# Copy the model and the prediction script
COPY ["predict.py", "model.bin", "./"]

# Expose the port Flask/Gunicorn will run on
EXPOSE 9696

# Define the command to run the service using Gunicorn [4, 5]
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]
