#Here add all required functions.
from _datetime import datetime

import pandas as pd


def cost_function(time,power,start,end):
    ''
    energy=0
    cost=0
    dt=(time[-1]-time[0])/len(time)
    newtime=time.copy()
    for timp in newtime:
        date_time_object=datetime.strftime(timp,'%H:%M:%S')
    for i in range(1,len(time)):
        energy+=power[i]*dt

def read_example_csv():
    df = pd.read_csv('example_data.csv', sep=' ', index_col=0, parse_dates=True)
    return df