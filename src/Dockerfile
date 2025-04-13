FROM python:3.12-slim

# environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# set working directory
WORKDIR /code

# install dependencies
COPY requirements.txt /code/
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

# copy application code
COPY . /code/

# expose the port for SSE server
EXPOSE 3000

# command to run the application
CMD ["python", "server.py"]

# create a non-root user and switch to it
RUN useradd -m appuser
USER appuser