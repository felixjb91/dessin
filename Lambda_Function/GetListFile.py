import boto3
import json

def getList(event,context):
        
    BUCKET_NAME = event['queryStringParameters']['BUCKET_NAME']
    s3 = boto3.resource("s3")
    
    bucket = s3.Bucket(BUCKET_NAME)
    listFile = bucket.objects.all();
    liste = []
    for obj in listFile:
        liste.append(obj.key)
    for key in liste:
        print(key)
 
    return {
        'statusCode' : 200,
        'headers': {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        'body' : json.dumps(liste)
    }