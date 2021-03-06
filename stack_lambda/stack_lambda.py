from aws_cdk import core as cdk
from aws_cdk import aws_lambda
from aws_cdk.aws_lambda_event_sources import SnsEventSource
from os import path, getcwd
from utils import generate_unique_id
from parameters import StackLambdaParameters


class StackLambda(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, sns_topic, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        stack_lambda_parameters = StackLambdaParameters()
        lambda_function_name = stack_lambda_parameters.build_parameter(
            self, 
            stack_lambda_parameters.PARAM_KEY_LAMBDA_FUNCTION_NAME
        ).value_as_string

        lambda_function = aws_lambda.Function(self, 
            id=generate_unique_id(),
            function_name=lambda_function_name,
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            code=aws_lambda.Code.from_asset(path.join(getcwd(), 'stack_lambda/functions')),
            handler='default_lambda_function.lambda_handler'
        )

        lambda_function.add_event_source(SnsEventSource(sns_topic))
