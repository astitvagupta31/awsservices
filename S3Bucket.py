import boto3

# S3 Bucket Services

# 1. S3 Bucket creation function 

s3 = boto3.resource('s3')


def create_bucket(name):
    s3.create_bucket(Bucket=name)
    
def delete_bucket(name):
    bucket = s3.Bucket(name)
    bucket.delete()

    
def list_bucket():
    li=[]
    for bucket in s3.buckets.all():
        li.append(bucket.name)
        print(bucket.name)
    return li    