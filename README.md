# cdk-lambda-sns

### What is this?
You should know first that AWS has [CDK](https://aws.amazon.com/cdk/) service (Cloud Development Kit). It basically helps you provision resources on AWS using your favorites language.

Behind the scene, it will actually convert your code into CloudFormation template.

This CDK configuration will generate followings
1. An SNS topic
2. A Lambda function which subscribe to the SNS topic
