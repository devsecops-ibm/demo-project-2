import logging
import json
import boto3
from botocore.exceptions import ClientError
import os

sm_client = boto3.client('secretsmanager')
response = sm_client.list_secrets(
)
print(response)