import json
import boto3

ec2client = boto3.client('ec2')

#print ec2client.describe_instances()

ec2res = ec2client.describe_instances()

for res in ec2res['Reservations']:
    for host in res['Instances']:
        print host['Tags']
        print host['PublicIpAddress']