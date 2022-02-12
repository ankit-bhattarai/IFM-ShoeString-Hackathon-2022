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


ex_threshold_dictionary = {"off" : [0,200], "idle" : [201,500], "on": [501]}
def state(current_power, threshold_dictionary):
  off_upper_limit = threshold_dictionary.get("off")[1]
  idle_lower_limit = off_upper_limit + 1
  idle_upper_limit = threshold_dictionary.get("idle")[1]
  on_lower_limit = idle_upper_limit + 1
  if (current_power >= on_lower_limit):
    return "On"
  elif (current_power >= 201):
    return "Idle"
  else:
    return "Off"
