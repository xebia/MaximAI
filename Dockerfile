# Use the official Python base image
FROM python:3.11-slim

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="$POETRY_HOME/bin:$PATH"

# Install Poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN pip install poetry

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY ./pyproject.toml /app/

# Install project dependencies
RUN poetry install --no-dev

# Copy the rest of the application files into the container
COPY ./src /app/src
COPY ./main.py /app/main.py

# Expose the port on which the application will run
EXPOSE 8080

# Set the PYTHONPATH to recognize the 'maximai' package
ENV PYTHONPATH="/app/src:$PYTHONPATH"

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]