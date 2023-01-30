from unittest.mock import MagicMock, patch

from module import lambda_handler


@patch("module.boto3")
def test_lambda_handler_with_patching(mock_boto3):
    # GIVEN

    # Replace the boto3.client("s3") instance with the mock s3 client
    mock_boto3.client("s3").head_bucket.return_value = {}

    # WHEN

    result = lambda_handler({}, MagicMock())

    # THEN

    assert result == {}
    mock_boto3.client("s3").head_bucket.assert_called_with(Bucket="service-bucket")
