import boto3

#session = boto3.session.Session()
#s3 = session.resource('s3')
s3 = boto3.resource('s3')

mybucket = input("Enter Your Bucket Name: ")

def list_obj(mybucket):
    for obj in s3.Bucket(mybucket).objects.all():
        print(obj.key)

list_obj(mybucket)