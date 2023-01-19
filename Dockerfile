FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip --no-cache-dir
RUN pip3 install -r requirements.txt --no-cache-dir
RUN django-admin startproject trydjango .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] 
