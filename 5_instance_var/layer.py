import boto3


class S3Interface:

    def __init__(self, bucket_name: str):
        self.s3 = boto3.client("s3")
        self.bucket_name = bucket_name

    def head_bucket(self) -> dict:
        return self.s3.head_bucket(Bucket=self.bucket_name)
