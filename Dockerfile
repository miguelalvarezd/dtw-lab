FROM python:3.12

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

# Install project dependencies without the code
RUN poetry install --no-root

# Copy the rest of the project
COPY . .

# Install the project and its modules
RUN poetry install

# Run the application
ENTRYPOINT ["poetry", "run", "start-server"]
