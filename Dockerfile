FROM python:3.11-slim

COPY ./app /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONPATH="."

RUN pip install pipenv && pipenv install --system --ignore-pipfile --dev

ENTRYPOINT ["/app/entrypoint.sh"]