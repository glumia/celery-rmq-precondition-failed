FROM python:3.13.2-alpine3.21

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["celery", "-A", "app", "worker", "--loglevel=info"]
