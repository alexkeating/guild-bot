FROM python:3.9-slim-buster as base

WORKDIR /service

RUN pip install poetry
COPY . /service

RUN poetry install
CMD python ./guild_bot



