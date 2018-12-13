import boto3
import json
    
def deleteFile(event,context):
    
    BUCKET_NAME = event['queryStringParameters']['BUCKET_NAME']
    FILE_NAME = event['queryStringParameters']['FILE_NAME']
    s3 = boto3.resource("s3")
    
    fileObj = s3.Object(BUCKET_NAME, FILE_NAME)
    fileObj.delete()

    return {
        'statusCode' : 200,
        'headers': {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        'body' : FILE_NAME+' a bien été supprimé à '+BUCKET_NAME
    }