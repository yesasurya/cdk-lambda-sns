from aws_cdk import core as cdk


DEFAULT_STACK_NAME_SNS = 'cdk-stack-sns'
DEFAULT_STACK_NAME_LAMBDA = 'cdk-stack-lambda'


class StackParameters():
    def __init__(self, stack_name, param_keys):
        self.stack_name = stack_name
        self.param_keys = param_keys

    def build_parameter(self, cdk_stack, key):
        return cdk.CfnParameter(cdk_stack, id=key)


class StackSnsParamaters(StackParameters):
    def __init__(self, stack_name=DEFAULT_STACK_NAME_SNS):        
        ## You can add parameter key for the stack here.
        ## Make sure to add the parameter key you added in the parameter keys list
        self.PARAM_KEY_SNS_TOPIC_NAME = 'snsTopicName'

        PARAM_KEYS = [
            self.PARAM_KEY_SNS_TOPIC_NAME
        ]

        super().__init__(stack_name, PARAM_KEYS)


class StackLambdaParameters(StackParameters):
    def __init__(self, stack_name=DEFAULT_STACK_NAME_LAMBDA):
        ## You can add parameter key for the stack here.
        ## Make sure to add the parameter key you added in the parameter keys list
        self.PARAM_KEY_LAMBDA_FUNCTION_NAME = 'lambdaFunctionName'

        PARAM_KEYS = [
            self.PARAM_KEY_LAMBDA_FUNCTION_NAME
        ]

        super().__init__(stack_name, PARAM_KEYS)
