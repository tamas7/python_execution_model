import pytest
from unittest.mock import MagicMock, patch


@pytest.mark.skip
@patch("layer.boto3")
def test_lambda_handler(mock_boto3):
    from module import lambda_handler

    # GIVEN

    # Replace the boto3.client("s3") instance with the mock s3 client
    mock_boto3.client("s3").head_bucket.return_value = {}

    # WHEN

    result = lambda_handler({}, MagicMock())

    # THEN

    assert result == {}
    mock_boto3.client("s3").head_bucket.assert_called_with(Bucket="service-bucket")
