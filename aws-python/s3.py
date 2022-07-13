import boto3
import time

session = boto3.session.Session()
s3 = session.resource('s3')

def list_buckets():
    print(f"Hello, cloud user. Here are your S3 buckets!\n")
    time.sleep(1)
    for bucket in s3.buckets.all():
        print(bucket.name)

list_buckets()

def list_obj(bucket_name):
    for obj in s3.Bucket(bucket_name).objects.all():
        print(obj.key)

list_obj('jaydenstaticwebsite')



