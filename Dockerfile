# Use official Python slim image
FROM python:3.10.4-slim-buster

# Update and install system dependencies
RUN apt update && apt upgrade -y && \
    apt-get install -y git curl python3-pip ffmpeg wget bash neofetch software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U pip wheel
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy all source code into container
COPY . .

# Set the command to run your Telegram bot
CMD ["python3", "-m", "main"]
