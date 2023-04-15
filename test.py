import Adafruit_DHT as dht_sensor
from prometheus_client import *
import time

h = Gauge("DHT11 humidity","")
temp = Gauge("DHT11 temp","")
def get_temperature_readings():
    humidity, temperature = dht_sensor.read_retry(dht_sensor.DHT11, 4)
    humidity = format(humidity, ".2f") + "%"
    temperature = format(temperature, ".2f") + "C"
    return {temperature,humidity}

while True:
    print(get_temperature_readings())
    time.sleep(1)