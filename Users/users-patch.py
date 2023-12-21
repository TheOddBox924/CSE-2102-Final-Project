import json
import boto3

#this function is for changing username only
#json object should be {"oldUser":"", "newUser":""}

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('StudentData')

def lambda_handler(event, context):
    try:
        # Extracting the JSON object from the request body
        request_body = json.loads(event["body"])
        
        # Extracting parameters from the JSON object
        old_username = request_body["oldUser"]
        new_username = request_body["newUser"]

        # Check if the item with the provided old username exists
        existing_item = table.get_item(Key={"username": old_username}).get("Item")

        if existing_item:
            # If the item exists, update only the username field
            table.update_item(
                Key={"username": old_username},
                UpdateExpression="SET #un = :new_username",
                ExpressionAttributeNames={"#un": "username"},
                ExpressionAttributeValues={":new_username": new_username}
            )
            
            # Return a success response
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Username updated successfully'})
            }
        else:
            # If the item does not exist, return an error response
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Item not found'})
            }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
