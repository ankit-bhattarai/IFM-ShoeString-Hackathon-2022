from datetime import datetime
from dotenv import load_dotenv, main
import os
import urllib3
urllib3.disable_warnings()
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

load_dotenv()
# You can generate a Token from the "Tokens Tab" in the UI
token = os.getenv('TOKEN')
org = os.getenv('ORG')
bucket = os.getenv('BUCKET')


class InfluxClient:
    def __init__(self, token=token, org=org, bucket=bucket):
        self._org = org
        self._bucket = bucket
        self._client = InfluxDBClient(url="https://europe-west1-1.gcp.cloud2.influxdata.com", token=token,
                                      verify_ssl=False, debug=False)

    def write_data(self, data, write_option=SYNCHRONOUS):
        write_api = self._client.write_api(write_option)
        write_api.write(self._bucket, self._org, data, write_precision='s')
