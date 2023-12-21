import json
import boto3
from decimal import Decimal

dynamodb_client = boto3.resource('dynamodb')
table = dynamodb_client.Table('courseSections')

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    param = event["queryStringParameters"]
    cid = param["cid"]  # Convert the search parameter to lowercase

    try:
        # Use the query operation to find all items with the specified courseID
        response = table.get_item(Key={'cid': cid})

        # Extract the items from the response
        items = response.get("Item", {}).get("sections", [])

        return {
            "statusCode": 200,
            "body": json.dumps(items, cls=DecimalEncoder)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
