import json
import boto3

r53client = boto3.client('route53')

r53res = r53client.list_hosted_zones_by_name()

print "\n"

for zone in r53res['HostedZones']:
    print zone['Name'][:-1] + " - " + zone['Id']
    for record in r53client.list_resource_record_sets(HostedZoneId=zone['Id'])['ResourceRecordSets']:
        if record['Name'] != zone['Name']:
            print record['Name'][:-1]
    print "-"*30+"\n"