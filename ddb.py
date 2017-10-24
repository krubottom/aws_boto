import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('edge-link-events')

response = table.query(
    IndexName='alarmActive-index',
    KeyConditionExpression=Key('alarmActive').eq('true')
)

for item in response['Items']:
    print item['eventID']
    #event = json.loads(dict(item))
    #print event
