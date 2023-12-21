import json
import boto3

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('courses')

eventTypes = {"post", "delete", "patch", "get"}

def item_maker(elem1, elem2, elem3, elem4, elem5, elem6, elem7):
    return {
        "cid": elem1,
        "title": elem2,
        "creditHours": elem3,
        "description": elem4,
        "prereqs": elem5,
        "openSections": elem6,
        "searchFilter":elem7
    }

def lambda_handler(event, context):
    try:
        action = event["routeKey"]
        body = json.loads(event['body'])
        

        courseID = body.get("cid")
        courseTitle = body.get("title")
        notes = body.get("creditHours")
        creditHours = body.get("description")
        courseCount = body.get("prereqs")
        preReqs = body.get("openSections")
        searchFilter = (courseID.lower() + " " + courseTitle.lower())
            # Assuming all fields are mandatory, add necessary validations
            
        response = table.put_item(Item=item_maker(courseID, courseTitle, notes, creditHours, courseCount, preReqs, searchFilter))
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Item added successfully"})
        }
        # Add conditions for other actions like DELETE, PATCH if needed
        
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid action"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }