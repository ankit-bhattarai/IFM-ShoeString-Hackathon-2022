"""
In this file we implement data collection from the raspberry pi and send it to a cloud. 
"""
import time
import board
import adafruit_ina260
import csv
from threading import Event, Thread
from influx_db import InfluxClient
from data import Sensor

i2c = board.I2C()
ina260 = adafruit_ina260.INA260(i2c)


def current_power():
    #return ina260.power
    return (ina260.voltage-3.3)*ina260.current/1000
    


Sensor1 = Sensor("Sensor1", "USB Fan")



def send_data_to_front_end():
    IC = InfluxClient()
    for index, sensor in enumerate([Sensor1]):
        sensor.update(current_power())
        print(ina260.voltage-3.3)
        IC.write_data(sensor.line_protocol())



#define how long do I want between each uplaod of data to the cloud
interval = 1

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        while not stopped.wait(interval): # the first call is in `interval` secs
            func(*args)
    Thread(target=loop).start()    
    return stopped.set
 


call_repeatedly(1, send_data_to_front_end)
