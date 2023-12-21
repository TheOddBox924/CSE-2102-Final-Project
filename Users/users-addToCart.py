import json
import boto3

dynamodb = boto3.resource('dynamodb')
users_table = dynamodb.Table('users')

def get_user_data(uid):
    response = users_table.get_item(Key={'uid': uid})
    return response.get('Item')

def lambda_handler(event, context):
    try:
        uid = event.get('requestContext', {}).get('authorizer', {}).get('jwt', {}).get('claims', {}).get('https://ss.com/email')

        body = json.loads(event['body'])
        cid = body.get('cid')
        section = body.get('section')
        print(body)
        user_data = get_user_data(uid)
        if user_data:
            item_to_add = {'cid': cid, 'sec': section}
            
            # Get user cart and assign it to a temporary variable
            cart = user_data.get('cart', [])
            print(user_data)
            print(cart)
            # Add the new item to the cart
            cart.append(item_to_add)
    
            # Update the user's cart in the database from the temorary variable.
            users_table.update_item(
                Key={'uid': uid},
                UpdateExpression='SET cart = :cart',
                ExpressionAttributeValues={':cart': cart}
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps('Item added to cart successfully!')
            }
        else:
            return {
                'statusCode': 404, 
                'body': json.dumps({'error': 'User not found'})}
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'An error occurred: {str(e)}')
        }
