import influxdb_client
import pandas as pd
from influxdb_client.client.write_api import SYNCHRONOUS

robots_df = pd.DataFrame(columns=["Robot Type", "Total Daily Energy", "Total Daily Cost", "Current Power", "Current State",
                                  "Duration on", "Expeced Times of Operation"])

total_power_df = pd.DataFrame(columns=["Total Power"], index=pd.DatetimeIndex([]))
token = 'SMVTNYq5kEoEgAXcqvKFlo9BZbKdyRiLcXPES3TGFBrsQZmChboUEgrbOD1cESm3237IEOaqOOnUwUMOkZt7BQ=='
org = 'ab2731@cam.ac.uk'
bucket = 'Sensor Data'
# Store the URL of your InfluxDB instance
url="https://europe-west1-1.gcp.cloud2.influxdata.com"
client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org, verify_ssl=False
)
query_api = client.query_api()
query = f' from(bucket:"Sensor Data")\
|> range(start: -30s)\
|> filter(fn:(r) => r._field == "{argument}" ) '
result = query_api.query(org=org, query=query)
results = []
for table in result:
  for record in table.records:
    power,timeq=record.__dict__['values']['_value'],record.__dict__['values']['_time']
    total_power_df.loc[timeq]=power
    print(power,timeq)


