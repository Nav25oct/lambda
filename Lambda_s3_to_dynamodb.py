import json

import boto3

# This script is to bring S3 json data to Dynamodb 

s3_client = boto3.client('s3')

dynamodb_client = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    print(event)
    

    ## Get S3 bucket and file name 
    
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    json_file_name = event['Records'][0]['s3']['object']['key']
    
    ##print(source_bucket)
    ##print(json_file_name)

    ## Read data from S3 
    
    json_object = s3_client.get_object(Bucket= source_bucket , Key = json_file_name)
    
    ##print(json_object)
    
    jsonFileReader = json_object['Body'].read()
    
    ##print(jsonFileReader)


    jsonDict = json.loads(jsonFileReader)

    
    table = dynamodb_client.Table('prescription')

    ### Insert data into Dynamodb table
    
    table.put_item(Item =jsonDict) 
    