FROM python:3.8.1-slim-buster

RUN useradd quser

# Port used by this container to serve HTTP.
EXPOSE 8000

ENV PYTHONUNBUFFERED=1 \
    PORT=8000

# Install system packages required by quser and Django.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    libpq-dev \
    libmariadbclient-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
 && rm -rf /var/lib/apt/lists/*

RUN pip install "gunicorn==20.0.4"

COPY requirements.txt /
RUN pip install -r /requirements.txt

WORKDIR /app

RUN chown quser:quser /app

COPY --chown=quser:quser . .

USER quser

RUN python manage.py collectstatic --noinput --clear

CMD set -xe; python manage.py migrate --noinput; gunicorn contents.wsgi:application
