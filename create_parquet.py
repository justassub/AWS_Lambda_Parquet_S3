from create_dataframe import create_df
from send_to_s3 import send


def create_and_write(file_name,
                     object_to_parquet: dict,
                     send_to_s3: bool = False,
                     s3_bucket: str = None,
                     s3_path: str = None,
                     compression="gzip",  # Can be: ['GZIP', 'UNCOMPRESSED']
                     location: str = "/tmp"
                     ):
    file_path: str = f"{location}/{file_name}.parquet"
    df = create_df(object_to_parquet)
    df.to_parquet(
        file_path,
        compression=compression
    )
    if send_to_s3:
        send(
            file_path,
            s3_bucket,
            s3_path
        )
