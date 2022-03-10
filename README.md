protocol


# create-lambda-s3-mail-service

We created a lambda service which send us an E-Mail, if we upload a file in s3.

- open sandbox
- create s3-Bucket
- -create a AWS-SNS Topic
  - subscripe 
    - select -Email and Write your E-Mail adress
    - confirm your E-Mail adress(confirm the subscription)
    - notice your arn (example [arn:aws:sns:us-west-2:643322559948:mytopic])
- create  in AWS Lambda a Lambda Function
  - Function name:"give your function name"
  - Runtime : Select Python 3.9
  - Permissions
    - Change default execition role
    - click "Use an existing Role"
    - select LambdaAccesRole
  - click "create function"


- select your Lambda Function
  - Add trigger
  - select s3
- create a new event
  - in event template, select "S3 Put"
- And Write your Code, 

```
import json
import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    message = "New file with name " + event['Records'][0]['s3']['object']['key']
    print(message)
    client.publish(TargetArn = "arn:aws:sns:us-west-2:590497118368:AlarmSet", Message = message)
```


# exercise2:

Build a Lambda Function whic count the words in a file and send you an E-Mail.
```
def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]
    response = s3client.get_object(
        Bucket = bucket,
        Key = key
        
        )

    data = response["Body"].read()
    words = data.split()
    numberofwords = len(words)
    #print(numberofwords)
  
    message = "The word count in the file {} is {} ".format(key, numberofwords)
    
    #print(message)
    client.publish(TargetArn = os.environ["topicArn"], Message = message)
    
```