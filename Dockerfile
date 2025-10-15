# Use the official Python image
FROM python:3.14-slim

# Set the working directory
WORKDIR /runner

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
	build-essential \
	curl

# Install Rust using rustup
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN export PATH="$PATH:/root/.cargo/bin"

# Install Poetry using the official installer
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy Poetry files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry install --no-interaction --no-ansi --no-root

# Only copy necessary files
COPY .env ./
COPY app ./app/

# Expose FastAPI default port
EXPOSE 8000

# Run FastAPI app (assumes main.py with app instance)
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]