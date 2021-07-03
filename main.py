import sys, getopt
import subprocess
from parameters import StackSnsParamaters, StackLambdaParameters


if __name__ == '__main__':
    stack_parameters = [StackSnsParamaters(), StackLambdaParameters()]

    _, args = getopt.getopt(sys.argv[1:], 'p', ["parameters"])
    args_dict = {}
    for arg in args:
        components = arg.split('=')
        key, value = components[0], components[1]
        args_dict[key] = value

    cdk_command_parameters = ''
    for stack_parameter in stack_parameters:
        for parameter in stack_parameter.param_keys:
            if parameter in args_dict.keys():
                cdk_command_parameters = '{0}--parameters {1}:{2}={3} '.format(
                    cdk_command_parameters, 
                    stack_parameter.stack_name, 
                    parameter,
                    args_dict[parameter]
                )
                del args_dict[parameter]
            else:
                raise Exception('Required parameter unspecified: {0}'.format(parameter))

    if len(args_dict) != 0:
        raise Exception('Redundant parameters not required by stack: {0}'.format(str(args_dict.keys())))

    cdk_command_parameters = cdk_command_parameters[:-1]
    cdk_command = 'cdk deploy --all --require-approval never ' + cdk_command_parameters
    popen = subprocess.Popen(cdk_command.split())
    popen.communicate(input='\n')
