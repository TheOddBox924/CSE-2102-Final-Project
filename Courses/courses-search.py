import json
import boto3
from decimal import Decimal

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('courses')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    param = event["queryStringParameters"]
    searchQuery = param["searchQuery"]  # Convert the search parameter to lowercase

    try:
        # Use the scan operation to find all items with the specified courseID containing the substring (case-insensitive)
        response = table.scan(
            FilterExpression="contains(searchFilter, :id)",
            ExpressionAttributeValues={
                ":id": searchQuery
            }
        )
        print(response)
        # Extract the items from the response
        items = response.get("Items", [])
        print(items)

        return {
            "statusCode": 200,
            "body": json.dumps(items, cls=DecimalEncoder)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
