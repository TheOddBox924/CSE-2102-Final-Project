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

DAYS = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

def day_to_index(day):
    return DAYS.index(day.lower()) if day.lower() in DAYS else "Invalid day of the week"

def get_user_data(uid):
    response = users_table.get_item(Key={'uid': uid})
    return response.get('Item')

def get_course_data(course):
    response = sections_table.get_item(Key={'cid': course['cid']})
    course_data = courses_table.get_item(Key={'cid': course['cid']}).get('Item')
    section_data = response['Item']['sections'][int(course['sec'])]
    course_data.update(section_data)
    course_data.update(course)  # Add cid and section to the response
    return course_data

def lambda_handler(event, context):
    try:
        uid = event.get('requestContext', {}).get('authorizer', {}).get('jwt', {}).get('claims', {}).get('https://ss.com/email')
        response_format = event.get('queryStringParameters', {}).get('format')

        user_data = get_user_data(uid)
        if user_data:
            enrolled_list = user_data.get('enrolled', [])
            course_data_list = [get_course_data(course) for course in enrolled_list]

            if response_format.lower() == "schedule":
                schedule_format = [[], [], [], [], [], [], []]
                for course_data in course_data_list:
                    schedule_format[day_to_index(course_data['day'])].append(course_data)
                items = schedule_format
            else:
                items = course_data_list

            return {
                'statusCode': 200,
                'body': json.dumps({'items': items}, cls=DecimalEncoder)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'User not found'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }