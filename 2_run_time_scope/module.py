import boto3
from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    print(f"Lambda handler: {event=}, {context=}")
    # boto3 client created in the function scope
    s3 = boto3.client("s3")
    return s3.head_bucket(Bucket="service-bucket")
