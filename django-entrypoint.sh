#!/bin/sh

until cd /app
do
    echo "Wainting for django volume.."
done

until python manage.py migrate
do
    echo "Waiting for db to be ready.."
    sleep 2
done

python manage.py collectstatic --noinput

# to create superuser
# python manage.py createsuperuser --noinput

# for prod
gunicorn spdjango.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

# for debug
python manage.py runserver
