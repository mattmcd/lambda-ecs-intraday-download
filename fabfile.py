import boto3
# Get constants from config file
from config import *

AWS_BUCKET = 'ftse100'
LAMBDA_FUN_NAME = 'ecs-download-launcher'
ECS_TASK_NAME = APP_NAME + 'Task'

# Define the role policy for Lambda execution
LAMBDA_EXEC_ROLE_NAME = APP_NAME + '-Lambda-Execution-Role'
LAMBDA_EXEC_ROLE_POLICY_NAME = 'AWSLambdaExecutionPolicy'
LAMBDA_EXEC_ROLE_POLICY = {
    'Version': '2012-10-17',
    'Statement': [
        {
            'Effect': 'Allow',
            'Action': [
                'logs:*',
                'ecs:RunTask'
            ],
            'Resource': [
                'arn:aws:logs:*:*:*',
                'arn:aws:ecs:*:*:*'
            ]
        }
    ]
}

# Define the trust policy
LAMBDA_EXEC_ROLE_TRUST_POLICY = {
    'Version': '2012-10-17',
    'Statement': [
        {
            'Sid': '',
            'Effect': 'Allow',
            'Principal': {
                'Service': 'lambda.amazonaws.com'
            },
            'Action': 'sts:AssumeRole'
        }
    ]
}

LAMBDA_FUN_CONFIG = {'task': ECS_TASK_NAME}

ECS_ROLE_BUCKET_ACCESS_POLICY_NAME = APP_NAME + 'BucketAccessPolicy'
