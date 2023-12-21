import json
import boto3

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('StudentData')

def lambda_handler(event, context):
    try:
        # Extracting the JSON object from the request body
        request_body = json.loads(event["body"])
        
        # Extracting the username from the JSON object
        username = request_body["username"]

        # Delete the item from DynamoDB based on the username
        response = table.delete_item(
            Key={"username": username}
        )

        # Check if the deletion was successful
        if response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            # Return a success response
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'User deleted successfully'})
            }
        else:
            # If the item does not exist, return a not found response
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
