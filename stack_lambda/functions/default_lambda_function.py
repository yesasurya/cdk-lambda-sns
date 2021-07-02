import json

def lambda_handler(event, context):
    sns_message = ''
    try:
        sns_message_str = event['Records'][0]['Sns']['Message']
        sns_message = json.loads(sns_message_str)
    except Exception as e:
        print(e)

    print(sns_message)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello, this is my SNS subscriber generated using CDK.')
    }
