import logging
import boto3
from botocore.exceptions import ClientError
import os

#   session = boto3.session.Session()
#   s3 = session.resource('s3')

s3_client = boto3.client('s3')
def upload_file(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
      
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
upload_file('testupload.txt','jaydenstaticwebsite')
    
    
