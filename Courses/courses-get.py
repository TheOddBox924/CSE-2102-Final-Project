import json
import boto3

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('courses')

def lambda_handler(event, context):
    try:
        # Extracting the JSON object from the request body
        request_body = json.loads(event["body"])
        
        # Extracting the course ID (cid) from the JSON object
        course_id = request_body.get("cid")

        # Retrieve the course from DynamoDB based on the course ID
        response = table.get_item(Key={"cid": course_id})

        # Check if the item exists
        if "Item" in response:
            # Extract the course details from the item
            course_details = response["Item"]

            # Return the course details in the response
            return {
                'statusCode': 200,
                'body': json.dumps({'course': course_details})
            }
        else:
            # If the item does not exist, return a not found response
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Course not found'})
            }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
