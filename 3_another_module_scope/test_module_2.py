import pytest
from unittest.mock import MagicMock


@pytest.fixture(autouse=True)
def init_s3(s3):
    s3.create_bucket(
        Bucket="service-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
    )


@pytest.fixture
def lambda_handler():
    from module import lambda_handler

    yield lambda_handler


def test_lambda_handler(lambda_handler):
    # WHEN

    result = lambda_handler({}, MagicMock())

    # THEN

    assert "ResponseMetadata" in result
