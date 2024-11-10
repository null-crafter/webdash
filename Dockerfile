FROM python:3.12.7-bookworm
RUN rm -rf /var/lib/apt/lists/* && pip install poetry && mkdir /app
WORKDIR /app
COPY . .
RUN poetry install
WORKDIR /app/src/webdash