import json
import boto3

TABLE_NAME = 'Robot-Status'

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="eu-central-1")

def lambda_handler(event, context):
    response1 = dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='Robot = :Robot',
        ExpressionAttributeValues={
        ':Robot': {'N': str(1)}
        }
    )
    
    response2 = dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='Robot = :Robot',
        ExpressionAttributeValues={
        ':Robot': {'N': str(2)}
        }
    )
    
    response3 = dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='Robot = :Robot',
        ExpressionAttributeValues={
        ':Robot': {'N': str(3)}
        }
    )
    string = f"Robot 1 status is {response1['Items'][0]['Status']['S']}\nRobot 2 status is {response2['Items'][0]['Status']['S']}\nRobot 3 status is {response3['Items'][0]['Status']['S']}"
    return{
        'statusCode': 200,
        'body': string
    }
