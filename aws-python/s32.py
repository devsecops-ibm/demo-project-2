import os
import boto3
import time

session = boto3.session.Session()
s3 = session.resource('s3')

obj_count = 0
mybucket = s3.Bucket('jaydenstaticwebsite') 
def count_obj():
    for i in mybucket.objects.all():
        print(i.key)
     #   obj_count = obj_count + 1
      #  print(obj_count)

count_obj()