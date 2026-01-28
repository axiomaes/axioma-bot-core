FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
# gcc and python3-dev might be needed for some python packages
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port (default for FastAPI/Uvicorn is 8000, but usually CapRover maps internal 80 or similar)
EXPOSE 80

# Command to run the application
# We use proper uvicorn launch command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
