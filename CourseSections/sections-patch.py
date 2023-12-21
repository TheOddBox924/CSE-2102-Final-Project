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
        new_start_time = request_body.get("newStartTime")
        new_end_time = request_body.get("newEndTime")

        # Perform DynamoDB update operation for courseSections table
        response = course_sections_table.update_item(
            Key={
                'cid': course_id,
                'sectionNO': section_number
            },
            UpdateExpression='SET startTime = :start, endTime = :end',
            ExpressionAttributeValues={
                ':start': new_start_time,
                ':end': new_end_time
            },
            ReturnValues='UPDATED_NEW'
        )

        # Return a success response with the updated item
        return {
            'statusCode': 200,
            'body': json.dumps(response['Attributes'])
        }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
