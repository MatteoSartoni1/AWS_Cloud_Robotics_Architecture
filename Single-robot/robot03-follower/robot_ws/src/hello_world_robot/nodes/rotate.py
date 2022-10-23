#!/usr/bin/env python

from geometry_msgs.msg import Twist
import rospy
import boto3
from boto3.dynamodb.conditions import Key
import signal
import time
import threading

TABLE_NAME = "Robot-Status"


class Rotator():
    
    # Creating the DynamoDB Client
    dynamodb_client = boto3.client('dynamodb', region_name="eu-central-1")

    # Creating the DynamoDB Table Resource
    dynamodb=boto3.resource('dynamodb', region_name="eu-central-1")
    table=dynamodb.Table(TABLE_NAME)
    
    def disconnecter(self):
            while True:
                response=self.dynamodb_client.query(
                    TableName=TABLE_NAME,
                    KeyConditionExpression='Robot = :Robot',
                    ExpressionAttributeValues={
                        ':Robot': {'N': str(3)}}
                )
                time.sleep(1.5)
                            
                if response['Items'][0]['Status']['S']=='disconnecting':
                    response=self.table.update_item(
                        Key={
                                'Robot': 3,
                                'Type':'Follower'
                            },
                            UpdateExpression = "set #st = :s",
                            ExpressionAttributeValues={":s" : "disconnected"},
                            ExpressionAttributeNames={"#st": "Status"},
                            ReturnValues="UPDATED_NEW"
                    )
                    self.twist = Twist()

                    r = rospy.Rate(10)
                    while not rospy.is_shutdown():
                        self.twist.angular.z = 0
                        self._cmd_pub.publish(self.twist)
                        rospy.loginfo('Rotating robot: %s', self.twist)
                        r.sleep() 
                    exit(1)
                time.sleep(2)
    
    def __init__(self):
        self._cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        
        # Use the DynamoDB client update the status of Robot 1
        response=self.table.update_item(
            Key={
                'Robot': 3,
                'Type':'Follower'
            },
            UpdateExpression = "set #st = :s",
            ExpressionAttributeValues={":s" : "connected"},
            ExpressionAttributeNames={"#st": "Status"},
            ReturnValues="UPDATED_NEW"
        )
        thread=threading.Thread(target=self.disconnecter, args=()) 
        thread.start()
                

    def rotate_forever(self):
        self.twist = Twist()
        r = rospy.Rate(10)
        
        while True:
            response=self.dynamodb_client.query(
                TableName=TABLE_NAME,
                KeyConditionExpression='Robot = :Robot',
                    ExpressionAttributeValues={
                        ':Robot': {'N': str(3)}}
                )
            if response['Items'][0]['Status']['S']=='connected':
                self.twist.angular.z = 0.1
                self._cmd_pub.publish(self.twist)
                rospy.loginfo('Rotating robot: %s', self.twist)
                r.sleep()
            time.sleep(2)
    
    
    def stopper(self):
        response=self.table.update_item(
        Key={
            'Robot': 3,
            'Type':'Follower'
        },
        UpdateExpression = "set #st = :s",
        ExpressionAttributeValues={":s" : "disconnected"},
        ExpressionAttributeNames={"#st": "Status"},
        ReturnValues="UPDATED_NEW"
    )
        self.twist = Twist()

        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            self.twist.angular.z = 0
            self._cmd_pub.publish(self.twist)
            rospy.loginfo('Rotating robot: %s', self.twist)
            r.sleep()    

def main():
    rospy.init_node('rotate')
    
    def handler(*args):
        rotator.stopper()
        exit(1)
    
    try:
        rotator = Rotator()
        signal.signal(signal.SIGINT, handler)
        rotator.rotate_forever()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()
