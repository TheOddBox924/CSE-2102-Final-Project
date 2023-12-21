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

        # Retrieve the item from DynamoDB based on the username
        response = table.get_item(Key={"username": username})

        # Check if the item exists
        if "Item" in response:
            # Extract the "enrolled" and "cart" lists from the item
            enrolled_list = response["Item"].get("enrolled", [])
            cart_list = response["Item"].get("cart", [])

            # Move items from "cart" to "enrolled"
            enrolled_list.extend(cart_list)

            # Clear the "cart" list
            cart_list.clear()

            # Update the DynamoDB item with the modified lists
            table.update_item(
                Key={"username": username},
                UpdateExpression="SET #enrolled = :enrolled, #cart = :cart",
                ExpressionAttributeNames={
                    "#enrolled": "enrolled",
                    "#cart": "cart"
                },
                ExpressionAttributeValues={
                    ":enrolled": enrolled_list,
                    ":cart": cart_list
                }
            )

            # Return the updated enrolled list in the response
            return {
                'statusCode': 200,
                'body': json.dumps({'enrolled': enrolled_list})
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
