from aws_cdk import core as cdk
from aws_cdk import aws_sns
from utils import generate_unique_id
from parameters import StackSnsParamaters


class StackSns(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack_sns_parameters = StackSnsParamaters()
        sns_topic_name = stack_sns_parameters.build_parameter(
            self, 
            stack_sns_parameters.PARAM_KEY_SNS_TOPIC_NAME
        ).value_as_string

        self.topic = aws_sns.Topic(self, 
            id=generate_unique_id(),
            topic_name=sns_topic_name
        )
