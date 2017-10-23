import json
import boto3

r53client = boto3.client('route53')

r53res = r53client.list_hosted_zones_by_name()

for zone in r53res['HostedZones']:
    print zone['Name'][:-1]