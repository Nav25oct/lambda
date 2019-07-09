import json
import boto3
import time
import urllib


print("Loading function")

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    print(source_bucket)
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    target_bucket = 'cur-octank'
    copy_source = {'Bucket':source_bucket, 'Key' : key }
    
    try:
        
        print("Waiting for the file persist in the source bucket")
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket,Key=key)
        print("Copying Object from soucre s3 bucket to target s3 bucket")
        s3.copy_object(Bucket=target_bucket, Key=key, CopySource=copy_source)
        
    except Exception as e:
        print(e)
        print("Error getting object {} from bucket {}")
        raise e