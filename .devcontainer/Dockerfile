FROM python:3.12-slim

# setup venv as default python environment
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Set up work directory
WORKDIR /workspace

# Install dependencies
COPY requirements-dev.txt ./

# Copy the app code
COPY . .