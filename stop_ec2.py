import boto3

# Create EC2 client
ec2 = boto3.client("ec2", region_name="ap-south-1")

# Get all running instances
response = ec2.describe_instances(
    Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"]
        },
        {
            "Name": "tag:AutoStop",
            "Values": ["true"]
        }
    ]
)

instance_ids = []

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        instance_ids.append(instance["InstanceId"])

# Stop instances
if instance_ids:
    print("Running instances found:")
    for instance_id in instance_ids:
        print(instance_id)

    print("\nStopping instances...")

    ec2.stop_instances(InstanceIds=instance_ids)

    print("All running EC2 instances have been stopped.")

else:
    print("No running EC2 instances found.")