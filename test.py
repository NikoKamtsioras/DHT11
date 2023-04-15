import Adafruit_DHT as dht_sensor
from prometheus_client import *
import time
global humidity
global temperature
humidity = 0
temperature = 0
h = Gauge("DHT11_humidity","")
temp = Gauge("DHT11_temp","")
def get_temperature_readings():
    humidity, temperature = dht_sensor.read_retry(dht_sensor.DHT11, 4)
    humidity = format(humidity, ".2f") + "%"
    temperature = format(temperature, ".2f") + "C"
    

while True:
    print(humidity)
    time.sleep(1)