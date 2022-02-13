import random
import time


from influx_db import InfluxClient
from data import Sensor
i = 0
Sensor1 = Sensor("Sensor1", "USB Fan")
Sensor2 = Sensor("Sensor2", "Robot")
Sensor3 = Sensor("Sensor3", "Lights")
Sensor4 = Sensor("Sensor4", "Computer 1")
Sensor5 = Sensor("Sensor5", "Computer 2")
while i < 8:
    sensor_data = random.sample(range(0, 150), 5) # We have 5 sensors
    IC = InfluxClient()
    for index, sensor in enumerate([Sensor1, Sensor2, Sensor3, Sensor4, Sensor5]):
        sensor.update(sensor_data[index])
        IC.write_data(sensor.line_protocol())
    i+= 1
    time.sleep(1.0)