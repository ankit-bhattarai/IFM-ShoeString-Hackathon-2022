# Here add all required functions.
import pandas as pd
import time


def cost_function(df, dt=1, start='08:30:00', end='22:30:00', low_price=0.08, high_price=0.121):
    low1 = df.between_time('00:00:00', start)
    high = df.between_time(start, end)
    low2 = df.between_time(end, '23:59:59')
    # Calculate energy consumption(kWh) during different periods
    energy_low = (low1.Power.sum() + low2.Power.sum()) / (36 * 10 ** 5)
    energy_high = (high.Power.sum()) / (36 * 10 ** 5)
    cost_low = energy_low * low_price
    cost_high = energy_high * high_price
    cost = cost_low + cost_high
    return cost


def read_example_csv():
    df = pd.read_csv('example_data.csv', sep=',', index_col=0, parse_dates=True)
    return df


def state(current_power, threshold_dictionary={"off": [0, 200], "idle": [201, 500], "on": [501]}):
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


def current_power(df):
    latest_time_df = df.index.max().strftime('%Y-%m-%d %X')
    total_current_power = latest_time_df.Power.sum()
    return total_current_power


def predict_cost(df):
    """need to upate"""
    return cost_function(df)
def total_energy(df):
    energy = (df.Power.sum()) / (36 * 10 ** 5)
    return energy

def summary(dataframe):
    total_energy1 = total_energy(dataframe)
    total_cost = cost_function(dataframe)
    instantaneous_power = current_power(dataframe)
    expected_cost = predict_cost(dataframe)
    data_dict = {"Total_Energy": total_energy1, "Total_cost": total_cost, "Current_Power": instantaneous_power,
                 "Expected_Cost": expected_cost}
    return data_dict


def cost_rate(time, energy):
    pass


class Summary:
    def __init__(self):
        self.instantaneous_power = 0
        self.energy_consumed = 0
        self.current_cost = 0
        self.expected_cost = 0

    def update(self, current_time, current_power):
        self.instantaneous_power = current_power
        self.energy_consumed += current_power * 1  # E = Pt
        self.cost += cost_rate(current_time, current_power)
        self.expected_cost = self.cost



def list_of_robots(df):
    list1=[]
    for i in range(len(df)):
        if df.Machine[i] not in list1:
            list1.append(df.Machine[i])
    return list1

def expected_savings(df, low_price=0.08, high_price=0.121):
  function = lambda row: row.peak_hour_energies * (high_price - low_price) if row.peak_hours <= 10 else 10*(row.peak_hour_energies/ row.peak_hours)*(high_price - low_price)
  results = df.apply(function, axis=1)
  return results
