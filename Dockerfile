FROM python:3.12-slim

# Install system dependencies, including Git and gnupg
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
ENV POETRY_VERSION=2.0.1
ENV POETRY_HOME=/opt/poetry
ENV PATH="${POETRY_HOME}/bin:${PATH}"
RUN curl -sSL https://install.python-poetry.org | python3 - --version ${POETRY_VERSION}

# Set the working directory
WORKDIR /app

# Copy the poetry.lock and pyproject.toml files
COPY poetry.lock pyproject.toml ./

# Install project dependencies
RUN poetry install --no-root

# Copy the rest of the project
COPY . .

# Run the application
CMD ["poetry", "run", "python", "main.py"]
