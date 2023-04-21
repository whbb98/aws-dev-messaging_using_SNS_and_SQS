import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1") 
bucket_name = "c73321a1486380l3983855t1w516620149088-s3bucket-3d438rbi8qo9"

policy_file = open("/home/ec2-user/environment/resources/public_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("Setting Permissions - DONE")