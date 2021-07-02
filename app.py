#####################
## README.short.md ##
#####################
## Below is a short documentation which may help you to run this program.

## Before running this program, please do the followings:
## 1. Configure your AWS credential using aws-cli. You can execute:
##     aws configure
## 2. Install all the requirements needed. You can execute:
##     pip3 install -r requirements.txt
## 3. Lambda accepts several ways of loading the code, e.g. from S3.
##    Fortunately, CDK offers you a feature where you can put your code in your local computer to be loaded into Lambda.
##    How does this work?
##    CDK will upload your code into an auto-generated S3 bucket and make a reference to that file, AUTOMATICALLY.
##    You just need to execute:
##     cdk bootstrap aws://unknown-account/unknown-region

## This app.py file is the main program, one that will run at the first time.
## For generating a CloudFormation template of all the stacks, you can execute:
##     cdk synth --all
## For deploying all the stacks, you can execute:
##     cdk deploy --all
## For destroying all the stacks, you can execute:
##     cdk destroy --all

## You may want to pass values which will be used in your stacks. These values are stored in a Context. 
## You may pass these values when you synthesize a CloudFormation template or when deploying to AWS.
## For example, if you want to pass values when you want to deploy to AWS, you can execute:
##     cdk deploy --all -c KEY1=VALUE1 -c KEY2=VALUE2
## In this program, you can pass SNS_TOPIC_NAME and LAMBDA_FUNCTION_NAME. You can execute:
##     cdk deploy --all -c SNS_TOPIC_NAME=<name> -c LAMBDA_FUNCTION_NAME=<name>


from aws_cdk import core
from stack_lambda.stack_lambda import StackLambda
from stack_sns.stack_sns import StackSns
import sys


DEFAULT_SNS_STACK_NAME = 'cdk-stack-sns'
DEFAULT_SNS_TOPIC_NAME = 'sns-default-topic'
DEFAULT_LAMBDA_STACK_NAME = 'cdk-stack-lambda'
DEFAULT_LAMBDA_FUNCTION_NAME = 'lambda-default-function'


if __name__ == '__main__':
    app = core.App()

    sns_topic_name = app.node.try_get_context('SNS_TOPIC_NAME')
    sns_topic_name = sns_topic_name if sns_topic_name is not None else DEFAULT_SNS_TOPIC_NAME
    lambda_function_name = app.node.try_get_context('LAMBDA_FUNCTION_NAME')
    lambda_function_name = lambda_function_name if lambda_function_name is not None else DEFAULT_LAMBDA_FUNCTION_NAME

    stack_sns = StackSns(app, DEFAULT_SNS_STACK_NAME, sns_topic_name=sns_topic_name)
    StackLambda(app, DEFAULT_LAMBDA_STACK_NAME, lambda_function_name=lambda_function_name, sns_topic=stack_sns.topic)
    app.synth()
