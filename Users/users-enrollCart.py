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

        user_data = get_user_data(uid)
        if user_data:
            # Get the current cart and enrolled courses
            cart = user_data.get('cart', [])
            enrolled = user_data.get('enrolled', [])
            
            # Combine the cart and enrolled courses
            new_enrolled = cart + enrolled
            
            # Update the enrolled courses in the database
            users_table.update_item(
                Key={'uid': uid},
                UpdateExpression='SET enrolled = :new_enrolled',
                ExpressionAttributeValues={':new_enrolled': new_enrolled}
            )
            
            # Clear the cart
            users_table.update_item(
                Key={'uid': uid},
                UpdateExpression='SET cart = :empty_cart',
                ExpressionAttributeValues={':empty_cart': []}
            )
            
            return {
                'statusCode': 200,
                'body': json.dumps('Cart merged into enrolled courses successfully!')
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
