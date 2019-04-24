import os
from .prod import *

# DEBUG = False

if os.environ.get('IGNORE_DJANGO_STORAGES') is None:
    INSTALLED_APPS += ['storages']

    STATICFILES_STORAGE = 'azure_devops.aws_storages.StaticS3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'azure_devops.aws_storages.MediaS3Boto3Storage'

    AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID')
    AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

    AWS_QUERYSTRING_AUTH = False

