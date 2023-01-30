import pytest
from moto import mock_s3

import boto3
from os import environ

AWS_REGION = "eu-west-1"


@pytest.fixture
def aws_credentials():
    environ["AWS_ACCESS_KEY_ID"] = "testing"
    environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    environ["AWS_SECURITY_TOKEN"] = "testing"
    environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def s3(aws_credentials):
    with mock_s3():
        yield boto3.client("s3", region_name=AWS_REGION)
