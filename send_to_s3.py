import boto3

s3 = boto3.client('s3')


def send(file_path: str, s3_bucket: str, s3_path: str):
    s3.upload_file(
        file_path,
        s3_bucket,
        s3_path
    )
