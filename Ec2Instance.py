import boto3

# EC2 Services Functions

# 1. Create an Ec2 Instance by create_instance() function 

def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId="ami-04505e74c0741db8d",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
    )

    print(instances["Instances"][0]["InstanceId"])

# 2. terminate an Ec2 Instance by terminate_instance() function 

def terminate_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)
    
# 3. Stop an Ec2 Instance by stop_instance() function 
    
def stop_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    print(response)    
    
# 4. Start an Ec2 Instance again by start_instance() function 
    
def start_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.start_instances(InstanceIds=[instance_id])
    print(response)      

# 5. get all running instnaces of Ec2 by get_running_instances() function 

def get_running_instances():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    reservations = ec2_client.describe_instances(Filters=[
        {
            "Name": "instance-state-name",
            "Values": ["running"],
        }
    ]).get("Reservations")
    list1=[]
    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            public_ip = instance["PublicIpAddress"]
            private_ip = instance["PrivateIpAddress"]
            dict1={}
            dict1["instance_id"]= instance_id
            dict1["instance_type"]=instance_type
            dict1["public_ip"]=public_ip
            dict1["private_ip"]=private_ip
            list1.append(dict1)
            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")    
    return list1         
            

