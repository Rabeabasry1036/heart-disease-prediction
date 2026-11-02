# Use Python 3.11 as the base image

FROM python:3.11-slim

# Set the working directory inside the container

WORKDIR /app

# Copy the requirements file

COPY requirements.txt .

# Install project dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code

COPY app/ ./app/

# Copy the trained machine learning model

COPY model/ ./model/

# Expose port 8000

EXPOSE 8000

# Start the FastAPI application

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
