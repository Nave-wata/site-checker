FROM python:3.12

# Set default values for UID and GID
ARG UID=1000
ARG GID=1000

# Create a non-root user to run the container with the specified UID and GID
RUN groupadd -g $GID scraper && \
    useradd -u $UID -g $GID -m -s /bin/bash scraper && \
    mkdir -p /app && \
    chown -R scraper:scraper /app

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Switch to the non-root user
USER scraper
