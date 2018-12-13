import boto3
import json
    
def getFile(event,context):
    
    BUCKET_NAME = event['queryStringParameters']['BUCKET_NAME']
    FILE_NAME = event['queryStringParameters']['FILE_NAME']
    s3 = boto3.client("s3")
    
    fileObj = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_NAME)
    return {
        'statusCode' : 200,
        'headers': {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        'body' : fileObj['Body'].read().decode('utf-8')
    }
