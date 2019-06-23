# AWS_Lambda_Parquets_S3
This package allows to save dict to Parquet file and store it to AWS s3 using AWS Lambda.

# FAQ:
How to use? <br>
Close repository -> add you lambda_handler script ->make *.zip -> upload to AWS lambda

What Linux version was used for? <br>
Linux kernel – 4.14.114-93.126.amzn2.x86_64 or 4.14.114-83.126.amzn1.x86_64
https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html

Lambda handler example ? 
```
def lambda_handler(event, context):
    create_and_write(
        file_name="abc",
        object_to_parquet={"test": "value"},
        send_to_s3=True,
        s3_bucket="s3_parquet_bucket",
        s3_path="parquet/2019-06-23"
    )
```

```
def lambda_handler(event, context):
    create_and_write(
        file_name="local_parquet",
        object_to_parquet={"test": "value"}     
    )
```

Why not boto3 library? <br/>
AWS Lambda server already has boto3 inside.

Why <b>fastparquet</b> and not <b>pyarrow</b>? <br/>
Pyarrow library is too large. Did not find any way to import from s3 ...
