from sense_hat import SenseHat
from update_bigquery import updateTable
import time

sense = SenseHat()

green = (0, 255, 0)
white = (255, 255, 255)

while True:
    humidity = sense.get_humidity()
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    errors = updateTable('innovation-factoy.Sense_Hat.test', temperature, pressure, humidity)
    if not errors:
        print('Rows have been added')
    else:
        print(f'Encountered errors while inserting rows: <errors>')
    time.sleep(1)
