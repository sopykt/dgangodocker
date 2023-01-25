from time import sleep
from celery import shared_task

@shared_task()
def long_task(lat_long):
    for i in range(1,10):
        print(f'Run {i} for {lat_long}')
        sleep(1)