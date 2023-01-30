import pytest
from unittest.mock import MagicMock


@pytest.fixture
def lambda_handler(s3):
    from module import lambda_handler

    s3.create_bucket(
        Bucket="service-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
    )

    yield lambda_handler


def test_lambda_handler(lambda_handler):
    # WHEN

    result = lambda_handler({}, MagicMock())

    # THEN

    assert "ResponseMetadata" in result
