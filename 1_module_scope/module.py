import boto3
from aws_lambda_powertools.utilities.typing import LambdaContext


# boto3 client is created in the module scope
s3 = boto3.client("s3")


def lambda_handler(event: dict, context: LambdaContext) -> dict:
    print(f"Lambda handler: {event=}, {context=}")
    return s3.head_bucket(Bucket="service-bucket")
