import time
import datetime
import timeit
#from pandas import datetime
from fit import fittiing
from dataframe import col
def countdown_timer(x, now=datetime.datetime.now):
    target = now()
    one_day_later = datetime.timedelta(days=1)
    for remaining in range(x, 0, -1):
        target += one_day_later
        print(datetime.timedelta(days=remaining), 'remaining', end='\r')
        time.sleep((target - now()).total_seconds())
    print('\nTIMER ended and I, as Artificial intelligence, will implement my job')

