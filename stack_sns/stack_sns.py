from aws_cdk import core as cdk
from aws_cdk import aws_sns


class StackSns(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, sns_topic_name, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.topic = aws_sns.Topic(self, 
            id=sns_topic_name,
            topic_name=sns_topic_name
        )
