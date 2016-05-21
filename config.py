# Constants

FULL_NAME_AND_EMAIL = 'Matt McDonnell <matt@matt-mcdonnell.com>'
APP_NAME = 'ECSIntradayDownloadWorker'

DOCKERHUB_USER = 'mattmcd'
DOCKERHUB_EMAIL = 'matt@matt-mcdonnell.com'
DOCKERHUB_IMAGE = 'pyanalysis'
DOCKERHUB_TAG = '{user}/{image}'.format(
    user=DOCKERHUB_USER, image=DOCKERHUB_IMAGE)

AWS_REGION = 'eu-west-1'
AWS_PROFILE = 'default'

ECS_CLUSTER = 'default'
