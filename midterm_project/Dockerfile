# Lightweight official Python base image
FROM python:3.14-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Define the working directory inside the container
WORKDIR /app

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' myuser && chown -R myuser /app
USER myuser

# Copy the dependencies file
COPY requirements.txt .

# Add route to .local/bin
ENV PATH=/home/myuser/.local/bin:$PATH

# Install dependencies (pandas, scikit-learn, flask, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the trained model artifact (saved by train.py)
COPY --chown=myuser model.bin .

# Copy the web service script
COPY --chown=myuser predict.py .

# Expose the port where the Flask application is running
EXPOSE 5000

# Define the command to run the web service using Python
CMD ["python", "predict.py"]