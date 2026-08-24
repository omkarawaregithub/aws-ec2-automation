import boto3

REGION = "ap-south-1"

ec2 = boto3.client("ec2", region_name=REGION)

# EC2 instances that you want to stop
instance_ids = [
    "i-0c31d1fae439897ae",
    "i-0378e3ec7e9182fdc"
]

print("Instances to stop:")

for instance_id in instance_ids:
    print(instance_id)

# Stop the specified instances
response = ec2.stop_instances(InstanceIds=instance_ids)

print("\nStop request sent successfully.")

for instance in response["StoppingInstances"]:
    print(
        f"{instance['InstanceId']}: "
        f"{instance['CurrentState']['Name']} -> "
        f"{instance['TargetState']['Name']}"
    )