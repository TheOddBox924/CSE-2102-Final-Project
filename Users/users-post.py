import json
import boto3

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('users')

def lambda_handler(event, context):
    try:
        # Extracting the JSON object from the request body
        request_body = json.loads(event["body"])
        
        # Extracting parameters from the JSON object
        uid = request_body["uid"]
        #user type is 0 (moderator), 1 (teacher), or 2(student), or 3(default/none)
        #(privileges correlate inversely with type #)
        # Constructing the item to be put into DynamoDB
        item = {
            "uid": uid,
            "enrolled": [],
            "cart": []
        }
        
        # Perform DynamoDB put operation
        response = table.put_item(Item=item)
        
        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item added successfully'})
        }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
