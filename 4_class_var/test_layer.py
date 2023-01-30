import pytest


@pytest.fixture(autouse=True)
def init_s3(s3):
    s3.create_bucket(
        Bucket="service-bucket",
        CreateBucketConfiguration={"LocationConstraint": "eu-west-1"},
    )


@pytest.fixture
def s3_interface(s3):
    from layer import S3Interface

    yield S3Interface(bucket_name="service-bucket")


def test_layer(s3_interface):
    # WHEN

    result = s3_interface.head_bucket()

    # THEN

    assert "ResponseMetadata" in result
