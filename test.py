import Adafruit_DHT as dht_sensor
from prometheus_client import *
import time

humidity = 0
temperature = 0
h = Gauge("DHT11_humidity","")
temp = Gauge("DHT11_temp","")
def get_temperature_readings():
    global humidity
    global temperature
    humidity, temperature = dht_sensor.read_retry(dht_sensor.DHT11, 4)
    humidity = format(humidity, ".2f") + "%"
    temperature = format(temperature, ".2f") + "C"
    

while True:
    get_temperature_readings()
    print(humidity)
    time.sleep(1)