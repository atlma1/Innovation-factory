from google.cloud import bigquery

client = bigquery.Client()
errors = client.query()