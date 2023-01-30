from unittest.mock import MagicMock, patch

# The module of the lambda_handler is imported in the module scope
import module


@patch("module.boto3", new=MagicMock())
def test_lambda_handler_with_patching():
    """
    Trying to patch the boto3 package import won't work, as it is defined in
    the module scope. This means that during import-time the s3 client is
    already defined as a boto3 client and not a MagicMock.
    """

    # The boto3 package is successfully mocked
    assert isinstance(module.boto3, MagicMock)
    # But the created s3 client object is not
    assert not isinstance(module.s3, MagicMock)


def test_mocking_the_client_object():
    """
    If the Lambda Function module is imported, can mock the AWS connection by
    replacing the S3 boto3 client with a mock object by overwriting the module
    attribute.
    """
    # GIVEN

    # Create mock object for the s3 client
    mock_s3 = MagicMock()
    # Assign a return value
    mock_s3.head_bucket.return_value = {}
    # Replace the boto3.client("s3") instance with the mock s3 client
    module.s3 = mock_s3

    # WHEN

    result = module.lambda_handler({}, MagicMock())

    # THEN

    assert result == {}
    mock_s3.head_bucket.assert_called_with(Bucket="service-bucket")
