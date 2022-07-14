import logging
import boto3
from botocore.exceptions import ClientError
import os

#s3.create_bucket(Bucket = 'jaydendynamicwebsite', CreateBucketConfiguration={
#        'LocationConstraint': 'ap-southeast-1'
#    })

bucketname = input("Enter your desired bucket name: ")
def createBucket(bucketname):
    s3 = boto3.resource('s3')
    try:
        response = s3.create_bucket(Bucket = bucketname, CreateBucketConfiguration={'LocationConstraint': 'ap-southeast-1'})
    except ClientError as e:
        logging.error(e)
        return False
    return True

createBucket(bucketname)