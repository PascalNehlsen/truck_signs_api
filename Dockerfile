# Base Image
FROM python:3.8.1

# Set working directory
WORKDIR /app

# Install netcat
RUN apt-get update && apt-get install -y netcat && apt-get clean

# Copy and install dependencies
COPY requirements.txt ${WORKDIR}
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy rest of the application code
COPY . ${WORKDIR}

# Make the entrypoint script executable
RUN chmod +x ./entrypoint.sh

# Expose the correct port (8020)
EXPOSE 8020

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]
