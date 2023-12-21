import json
import boto3

dynamodb_client = boto3.resource('dynamodb')
course_sections_table = dynamodb_client.Table('courseSections')

def lambda_handler(event, context):
    try:
        # Extracting the JSON object from the request body
        request_body = json.loads(event["body"])

        # Extracting course section details from the JSON object
        course_id = request_body.get("cid")
        section_number = request_body.get("sectionNO")

        # Perform DynamoDB get operation for courseSections table
        response = course_sections_table.get_item(
            Key={
                'cid': course_id,
                'sectionNO': section_number
            }
        )

        # Check if the item exists
        if 'Item' in response:
            # Return the item details
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            # Return a not found response
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Course section not found'})
            }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
