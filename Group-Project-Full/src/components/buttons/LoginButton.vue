<template>
    <button class="button__login" @click="handleLogin">Log In</button>
  </template>
  
  <script setup>
  import { useAuth0 } from "@auth0/auth0-vue";
  
  const { loginWithRedirect } = useAuth0();
  
  const handleLogin = () => {
    loginWithRedirect({
      appState: {
        target: "/managecourses",
      },
    });
  };
  </script>
  /**
  
  
  import json
import boto3

dynamodb_client = boto3.resource('dynamodb')
users_table = dynamodb_client.Table('users')
sections_table = dynamodb_client.Table('courseSections')

def day_to_index(day):
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day = day.lower()
    if day in days:
        return days.index(day)
    else:
        return "Invalid day of the week"

def lambda_handler(event, context):
    try:
        # Extracting the username from the event
        uid = event.get('requestContext', {}).get('authorizer', {}).get('jwt', {}).get('claims', {}).get('https://ss.com/email')
        response_format = event.get('queryStringParameters', {}).get('format')

        # Retrieve the item from DynamoDB based on the username
        response = users_table.get_item(Key={'uid': uid})
        
        print(response)
        # Check if the item exists
        if 'Item' in response:
            # For storing section data of all the sections the user is enrolled in
            standard_format = []
            schedule_format = [[], [], [], [], [], [], []]
            # Extract the 'enrolled' list from the item
            enrolled_list = response['Item'].get('enrolled', [])
            
            # Get section data from cid's in enrolled_list
            for course in enrolled_list:
                print(course)
                response = sections_table.get_item(Key={'cid': course['cid']})
                print(response)
                course_data = response['Item']['sections'][int(course['sec'])]
                if (response_format.lower() == "standard"):
                    standard_format.append(course_data)
                elif (response_format.lower() == "schedule"):
                    print(course_data)
                    schedule_format[day_to_index(course_data['day'])].append(course_data)
                else:
                    return {
                        'statusCode': 500,
                        'body': json.dumps({'error': 'invalid response_format. Valid values are: standard, schedule'})
                    }
                    
            # Return the enrolled list in the response
            if response_format.lower() == "standard":
                return {
                    'statusCode': 200,
                    'body': json.dumps({'items': standard_format})
                }
            else:
                return {
                    'statusCode': 200,
                    'body': json.dumps({'items': schedule_format})
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
  
  */