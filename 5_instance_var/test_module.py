import pytest
from unittest.mock import MagicMock

from module import lambda_handler


@pytest.fixture(autouse=True)
def init_s3(s3):
    s3.create_bucket(
        Bucket="service-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
    )


def test_lambda_handler():
    # WHEN

    result = lambda_handler({}, MagicMock())

    # THEN

    assert "ResponseMetadata" in result
