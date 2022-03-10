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