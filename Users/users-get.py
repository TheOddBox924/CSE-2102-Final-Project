import json
import boto3

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('users')

def lambda_handler(event, context):
    try:
        # Extracting the JSON object from the request body
        uid = event.get('requestContext', {}).get('authorizer', {}).get('jwt', {}).get('claims', {}).get('https://ss.com/email')
        
        # Perform DynamoDB operation
        response = table.get_item(Key={"uid": uid})
        
        # Return the DynamoDB response
        return {
            'statusCode': 200,
            'body': json.dumps(response["Item"])
        }
    except Exception as e:
        # Return an error response
        if str(e) == "'Item'":
            return {
                'statusCode': 500,
                'body': json.dumps({'error': 'User not found', "uid": str(uid)})
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({'error': str(e), "uid": str(uid)})
            }
