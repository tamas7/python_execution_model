import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_s3():
    return MagicMock()


@pytest.fixture
def lambda_handler(mock_s3):
    import module

    module.s3 = mock_s3

    yield module.lambda_handler


def test_mocking_the_client_object(lambda_handler, mock_s3):
    """
    If the Lambda Function module is imported, can mock the AWS connection by
    replacing the S3 boto3 client with a mock object by overwriting the module
    attribute.
    """

    # GIVEN

    mock_s3.head_bucket.return_value = {}

    # WHEN

    result = lambda_handler({}, MagicMock())

    # THEN

    assert result == {}
    mock_s3.head_bucket.assert_called_with(Bucket="service-bucket")
