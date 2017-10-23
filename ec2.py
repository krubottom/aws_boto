import json
import boto3

ec2client = boto3.client('ec2')

ec2res = ec2client.describe_instances()

def get_instance_name(ec2id):
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(ec2id)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return instancename


for res in ec2res['Reservations']:
    for instance in res['Instances']:
        print get_instance_name(instance['InstanceId']) + " - " + instance['PublicIpAddress']