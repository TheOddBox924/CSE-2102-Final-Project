import json
import boto3

dynamodb_client = boto3.resource('dynamodb')
course_sections_table = dynamodb_client.Table('courseSections')

def lambda_handler(event, context):
    try:
        # Extracting the JSON object from the request body
        request_body = json.loads(event["body"])

        # Extracting course details from the JSON object
        course_id = request_body.get("cid")

        # Perform DynamoDB query operation for courseSections table
        response = course_sections_table.query(
            KeyConditionExpression='cid = :cid',
            ExpressionAttributeValues={
                ':cid': course_id
            }
        )

        # Check if there are matching items
        if 'Items' in response and response['Items']:
            # Return the list of matching items
            return {
                'statusCode': 200,
                'body': json.dumps(response['Items'])
            }
        else:
            # Return a not found response
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'No matching course sections found'})
            }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
