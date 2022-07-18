import logging
import boto3
from botocore.exceptions import ClientError
import os
    
s3_client = boto3.client('s3')
def del_obj(bucket,key):
    try:
        response = s3_client.delete_object(
            Bucket= bucket,
            Key= key,
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True

del_obj('jaydenstaticwebsite','testupload.txt')