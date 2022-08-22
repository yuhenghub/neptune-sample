import requests


def lambda_handler(event, context):
    url = event['url']
    payload = '{"source":\"'+event['s3']+'\","format": "csv","iamRoleArn": \"'+event['role']+'\","region": \"'+event['region']+'\","failOnError": "TRUE","parallelism": "MEDIUM","updateSingleCardinalityProperties": "FALSE","queueRequest": "TRUE"}'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=payload, headers=headers)
    return r.text