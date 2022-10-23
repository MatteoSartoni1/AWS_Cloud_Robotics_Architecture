The REST API, which displays the robots' status in a web page, has been developed through the integration of AWS Lambda and Amazon API Gateway.

![api](https://user-images.githubusercontent.com/90899031/197400379-4b769205-c7b2-4eb4-9ebe-d227e8d74f07.png)


First an AWS Lambda function, which retrives the status from the database, has been built usign the lambda.py script. Subsequently a REST API has been created using Amazon API Gateway. Through the GET method it was possible to invoke the aforementioned Lambda function
