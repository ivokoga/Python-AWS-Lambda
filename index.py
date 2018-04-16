import json
import datetime


def handler(event, context):
    data = {
        'output': 'Hello World 2',
        'timestamp': datetime.datetime.utcnow().isoformat(),
        'name': 'Koga'
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
