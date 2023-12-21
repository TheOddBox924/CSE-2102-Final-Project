import json
import boto3
from decimal import Decimal


dynamodb_client = boto3.resource('dynamodb')
users_table = dynamodb_client.Table('users')
sections_table = dynamodb_client.Table('courseSections')
courses_table = dynamodb_client.Table('courses')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    try:
        # Extracting the username from the event
        uid = event.get('requestContext', {}).get('authorizer', {}).get('jwt', {}).get('claims', {}).get('https://ss.com/email')
        # Retrieve the item from DynamoDB based on the username
        response = users_table.get_item(Key={'uid': uid})
        
        print(response)
        # Check if the item exists
        if 'Item' in response:
            # For storing section data of all the sections the user is enrolled in
            data = []
            # Extract the 'enrolled' list from the item
            enrolled_list = response['Item'].get('cart', [])
            # Get section data from cid's in enrolled_list
            print(enrolled_list)
            for course in enrolled_list:
                print(course)
                section = sections_table.get_item(Key={'cid': course['cid']})
                course_data = courses_table.get_item(Key={'cid': course['cid']})
                print(response)
                item = {
                    'cid': course['cid'],
                    'sec': course['sec'],
                    'course_data': course_data['Item'],
                    'section_data': section['Item']['sections'][int(course['sec'])]
                }
                data.append(item)
            # Return the enrolled list in the response
            return {
                'statusCode': 200,
                'body': json.dumps({'items': data}, cls=DecimalEncoder)
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
