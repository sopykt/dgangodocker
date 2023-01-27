#!/bin/sh
until cd /app
do
    echo "Wainting for django volume.."
done

celery -A spdjango worker -l info