import requests


def lambda_handler(event, context):
    url = event['url']
    payload = '{"gremlin": "g.V(\''+event['errorcode']+'\').hasLabel(\'ErrorCode\').out(\'occurs_when\').out(\'is_attached_of\').out(\'is_part_of\').path().by(valueMap(\'name\'))"}'
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url, data=payload, headers=headers)
    print(r.text)
    return r.text
