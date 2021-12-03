import time
import Adafruit_CircuitPython_DHT as dht

sensor = dht.DHT11
pin = 18

try:
    while True:
        h, t = dht.read_retry(sensor, pin)
        if h is not None and t is not None:
            print("Temp = {0:0.1f}*C Humi = {1:0.1f}%".format(t,h))
        else:
            print("Read error")
        time.sleep(1)
except KeyboardInterrupt:
    print("키보드 인터럽트 발생")
