FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . .
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 
