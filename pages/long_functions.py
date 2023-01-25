from time import sleep

def long_task():
    for i in range(1,10):
        print(f'Run {i}')
        sleep(1)