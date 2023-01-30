import boto3

# boto3 client is created in the module scope
s3 = boto3.client("s3")


class S3Interface:
    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name

    def head_bucket(self) -> dict:
        return s3.head_bucket(Bucket=self.bucket_name)
