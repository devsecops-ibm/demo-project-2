import boto3

session = boto3.session.Session()
s3 = session.resource('s3')

def list_obj(mybucket):
    for obj in s3.Bucket(mybucket).objects.all():
        print(obj.key)

list_obj('jaydenstaticwebsite')