The REST API, which displays the robots' status in a web page, has been developed through the integration of AWS Lambda and Amazon API Gateway.

First an AWS Lambda function, which retrives the status from the database, has been built usign the lambda.py script. Subsequently a REST API has been created using Amazon API Gateway. Through the GET method it was possible to invoke the aforementioned Lambda function
