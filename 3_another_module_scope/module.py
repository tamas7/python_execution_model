from aws_lambda_powertools.utilities.typing import LambdaContext

from layer import S3Interface


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    print(f"Lambda handler: {event=}, {context=}")
    # boto3 client is created in another module
    s3 = S3Interface(bucket_name="service-bucket")
    return s3.head_bucket()
