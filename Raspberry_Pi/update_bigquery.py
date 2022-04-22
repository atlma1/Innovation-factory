from google.cloud import bigquery
import os
from datetime import datetime


credentials_path = 'Private_Key_Google_Cloud.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

Project = 'innovation-factory'
Dataset = 'innovation-factoy.Sense_Hat'
Table ='innovation-factoy.Sense_Hat.test'


def updateTable(tableId, temp, pressure, humidity, timeSince):
    client = bigquery.Client()
    dateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time = datetime.now().strftime('%H:%M:%S')
    print(time)

    rows_to_insert = [
        {u'Temperature': temp, u'Pressure': pressure, u'Humidity': humidity, u'DATETIME': dateTime, u'TIME': time, u'time_since_start': timeSince}
    ]
    errors = client.insert_rows_json(tableId, rows_to_insert)
    if not errors:
        print('Rows have been added')
    else:
        print(f'Encountered errors while inserting rows: <errors>')
        print (errors)


# updateTable("innovation-factoy.Sense_Hat.test", 20, 20, 20)






