#!/usr/bin/env python3

import boto3
from boto3.dynamodb.conditions import Key
import time

while True:
    
    TABLE_NAME = "Robot-Status"
   
    # Creating the DynamoDB Client
    dynamodb_client = boto3.client('dynamodb',region_name="eu-central-1",
    aws_access_key_id="xxxx",aws_secret_access_key="xxxx")

    # Creating the DynamoDB Table Resource
    dynamodb=boto3.resource('dynamodb',region_name="eu-central-1",
    aws_access_key_id="xxxx",aws_secret_access_key="xxxx")
    table=dynamodb.Table(TABLE_NAME)
    
    # Use the DynamoDB client get item method to get a single item
    response1=dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='Robot = :Robot',
        ExpressionAttributeValues={
        ':Robot': {'N': str(1)}
        }
    )
    print(response1['Items'][0]['Status']['S'])
    # Use the DynamoDB client get item method to get a single item
    response2=dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='Robot = :Robot',
        ExpressionAttributeValues={
        ':Robot': {'N': str(2)}
        }
    )
    
    print(response2['Items'][0]['Status']['S'])
    # Use the DynamoDB client get item method to get a single item
    response3=dynamodb_client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression='Robot = :Robot',
        ExpressionAttributeValues={
        ':Robot': {'N': str(3)}
        }
    )
    print(response3['Items'][0]['Status']['S'])
    
    if response1['Items'][0]['Status']['S'] == "disconnected" and response2['Items'][0]['Status']['S'] == "connected":
        response2 = table.update_item(
            Key={
                'Robot': 2,
                'Type':'Follower'
                },
                UpdateExpression = "set #st = :s",
                ExpressionAttributeValues={":s" : "disconnecting"},
                ExpressionAttributeNames={"#st":"Status"},
                ReturnValues="UPDATED_NEW"
            )
    
    if response1['Items'][0]['Status']['S'] == "disconnected" and response3['Items'][0]['Status']['S'] == "connected":
        response3 = table.update_item(
            Key={
                'Robot': 3,
                'Type':'Follower'
                },
                UpdateExpression = "set #st = :s",
                ExpressionAttributeValues={":s" : "disconnecting"},
                ExpressionAttributeNames={"#st":"Status"},
                ReturnValues="UPDATED_NEW"
            )
    time.sleep(0.5)
