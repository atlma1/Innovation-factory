from sense_hat import SenseHat
from StreamToBigQuery import updateTable
import time

sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)

while True:
    humidity = sense.humidity
    humidity_value = 64 * humidity / 100
    temperature = sense.temperature
    pressure = sense.pressure
    updateTable('innovation-factoy.Sense_Hat.test', temperature, pressure, humidity)
    time.sleep(1)
