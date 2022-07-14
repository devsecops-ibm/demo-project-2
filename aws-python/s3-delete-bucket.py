import logging
import boto3
from botocore.exceptions import ClientError
import os

#s3.create_bucket(Bucket = 'jaydendynamicwebsite', CreateBucketConfiguration={
#        'LocationConstraint': 'ap-southeast-1'
#    })

AWS_REGION = "ap-southeast-1"
bucketname = input("Enter the name of the bucket you want to delete: ")
def createBucket(bucketname):
    s3 = boto3.client('s3', region_name=AWS_REGION)
    try:
        response = s3.delete_bucket(Bucket = bucketname)
    except ClientError as e:
        logging.error(e)
        return False
    return True

createBucket(bucketname)