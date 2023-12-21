import json
import boto3

#kill a course by cid

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('courses')

def lambda_handler(event, context):
    try:
        # Extracting the JSON object from the request body
        request_body = json.loads(event["body"])
        
        # Extracting the course ID (cid) from the JSON object
        course_id = request_body.get("cid")

        # Delete the item from DynamoDB based on the course ID
        response = table.delete_item(
            Key={"cid": course_id}
        )

        # Check if the deletion was successful
        if response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            # Return a success response
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Course deleted successfully'})
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
