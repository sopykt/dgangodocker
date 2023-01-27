FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --upgrade pip --no-cache-dir
RUN pip install gunicorn
RUN pip install -r requirements.txt --no-cache-dir
RUN chmod +x celery-entrypoint.sh
RUN chmod +x django-entrypoint.sh
