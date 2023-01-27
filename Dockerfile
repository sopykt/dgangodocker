FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
# Install dos2unix to fix line ending errors
RUN apt-get update && apt-get install -y dos2unix
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements_prod.txt --no-cache-dir
RUN mv spdjango/settings_prod.py spdjango/settings.py
RUN dos2unix celery-entrypoint.sh
RUN dos2unix django-entrypoint.sh
RUN chmod +x celery-entrypoint.sh
RUN chmod +x django-entrypoint.sh
