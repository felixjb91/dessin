import boto3
import json
    
def createFile(event,context):

    dict_input = json.loads(event['body'])
 
    BUCKET_NAME = dict_input['bucket']
    FILE_NAME = dict_input['filename']
    CONTENT_FILE = json.dumps(dict_input['body'])

    
    s3 = boto3.client("s3")
    
    response = s3.put_object(
        ACL='public-read-write',
        Body=CONTENT_FILE,
        Bucket=BUCKET_NAME,
        Key=FILE_NAME
    )

    return {
        'statusCode' : 200,
        'headers': {
            'Content-Type': 'application/json', 
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type,Authorization,Upgrade-Insecure-Requests,X-Requested-With, Origin,Accept,Access-Control-Allow-Headers,Access-Control-Allow-Methods, Accept',
            'Access-Control-Allow-Credentials': 'true'
        },
        'body' : FILE_NAME+' a bien été ajouté à '+BUCKET_NAME+ ' CONTENT_FILE : '+ CONTENT_FILE

    }
        