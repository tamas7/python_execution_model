import boto3


class S3Interface:
    # boto3 client is created in the class body scope
    s3 = boto3.client("s3")

    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def head_bucket(self) -> dict:
        return self.s3.head_bucket(Bucket=self.bucket_name)
