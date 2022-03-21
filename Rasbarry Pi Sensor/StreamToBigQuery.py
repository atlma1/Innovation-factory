from google.cloud import bigquery_storage_v1
from google.cloud import bigquery
import os


credentials_path = '/Rasbarry Pi Sensor/Private Key for Google cloud.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

Project = 'innovation-factory'
Dataset = 'innovation-factoy.Sense_Hat'
Table ='innovation-factoy.Sense_Hat.test'

def updateTable(tableId, temp, pressure, humidity):
    client = bigquery.Client()
    table_id= tableId
    rows_to_insert = [
        {u'Temperature': temp, u'Pressure': pressure, u'Humidity': humidity}
    ]

    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print('Rows have been added')
    else:
        print(f'Encountered errors while inserting rows: <errors>')




updateTable(Table, 20, 322, 40)





