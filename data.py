import datetime
from datetime import time


def cost_rate(current_time, power, low_time=(8, 30), high_time=(22, 30), low_rate=0.08, high_rate=0.121):
    """ Function which calculates the current cost in £ based on whether it is during times of high rate or low rate"""
    if time(*low_time) <= current_time <= time(*high_time):
        # Between the low time and high time so operating in times of peak electricity
        cost = high_rate * power
    else:
        cost = low_rate * power
    return cost


class Sensor:
    def __init__(self, name, use_type, idle_power=10, on_power=100, lower_time_threshold=(2, 30),
                 upper_time_threshold=(8, 30)):
        self.name = name
        self.use_type = use_type
        self.state = "Off"
        self.idle_power = idle_power
        self.on_power = on_power
        self.lower_time_threshold = time(*lower_time_threshold)
        self.upper_time_threshold = time(*upper_time_threshold)
        self.energy_consumed = 0
        self.instantaneous_power = 0
        self.current_cost = 0
        self.expected_cost = 0

    def update(self, current_power):
        self.instantaneous_power = current_power
        self.energy_consumed += current_power * 1  # E = Pt
        self.current_cost += cost_rate(datetime.datetime.now().time(), current_power)
        self.expected_cost = self.current_cost
        self.update_current_state()

    def update_current_state(self):
        if self.instantaneous_power < self.idle_power:
            self.state = "Off"
        elif self.instantaneous_power < self.on_power:
            self.state = "Idle"
        else:
            self.state = "On"

    def line_protocol(self):
        return "{},sensor={},state={} power={},daily_energy={},daily_cost={:.3f},expected_cost={:.3f}".format(self.name, self.name, self.state, self.instantaneous_power, self.energy_consumed, self.current_cost, self.expected_cost)

