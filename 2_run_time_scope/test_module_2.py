import pytest
from moto import mock_s3
from unittest.mock import MagicMock

import boto3


@pytest.fixture
def lambda_handler():
    with mock_s3():
        from module import lambda_handler

        s3 = boto3.client("s3")
        s3.create_bucket(
            Bucket="service-bucket",
            CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
        )

        yield lambda_handler


def test_lambda_handler_with_patching(lambda_handler):
    # WHEN

    result = lambda_handler({}, MagicMock())

    # THEN

    assert "ResponseMetadata" in result
