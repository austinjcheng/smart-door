import json
import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):

    client = boto3.resource('dynamodb')
    table = client.Table('DB1') # Change if your DB name differs
    
    otp = event['body']
    # strip the first 4 characters
    otp = otp[4:]
    
    response = table.get_item(
        Key={
            'passcode': otp
        }
    )
    if response.get("Item"):
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": { },
            "body": json.dumps("passed")
        }
    else:
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": { },
            "body": json.dumps("failed")
        }
        
