import influxdb_client
import pandas as pd
import numpy as np
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
    org=org
)
query_api = client.query_api()
query = ' from(bucket:"Sensor Data")\
|> range(start: -30m)\
|> filter(fn:(r) => r._field == "power" ) '
result = query_api.query(org=org, query=query)
results = []
for table in result[:4]:
  for record in table.records:
    #print(record)
    results.append( record.get_value())
    #total_power_df[]=
#length = len(results)
#times = np.arange(length)
#print(times)
print(results)