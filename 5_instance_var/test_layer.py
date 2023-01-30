import pytest

from layer import S3Interface


@pytest.fixture(autouse=True)
def init_s3(s3):
    s3.create_bucket(
        Bucket="service-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
    )


def test_layer(s3):
    # GIVEN

    s3_interface = S3Interface(bucket_name="service-bucket")

    # WHEN

    result = s3_interface.head_bucket()

    # THEN

    assert "ResponseMetadata" in result
