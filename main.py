
import time
from datetime import datetime, timedelta
import datetime
from timing import countdown_timer
from model import mod
from dataframe import col
from fit import fittiing
import pickle
import pandas as pd
from fit import incremental_learning

class Time_series_cities:
    def loo(self):
        while(True):
            countdown_timer(1)
            print("The system is about to update itself")
            incremental_learning(1)# CITY_ID
            mod() #ALL_CITIES
            countdown_timer(1)
            print("The system is about to update itself")
            incremental_learning(2)
            mod()
            countdown_timer(1)
            print("The system is about to update itself")
            incremental_learning(3)
            mod()
            countdown_timer(1)
            print("The system is about to update itself")
            incremental_learning(4)
            mod()
            countdown_timer(1)
            print("The system is about to update itself")
            incremental_learning(5)
            mod()
            countdown_timer(1)
            print("The system is about to update itself")
            incremental_learning(6)
            print("The system is about to update itself")
            mod()
            '''
            print("The system is about to update itself")
            incremental_learning(1)
            incremental_learning(2)
            incremental_learning(3)
            incremental_learning(4)
            incremental_learning(5)
            incremental_learning(6)
            mod()
            '''







implement=Time_series_cities()
implement.loo()

