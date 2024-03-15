import os

import pandas as pd
from dotenv import load_dotenv
from google.cloud import bigquery, storage

# At first, we need to load the .env file to get the environment variables
# From .env file
load_dotenv()
# Project ID from GCP
project_id = os.getenv("PROJECT_ID")
# Bucket name from Google Cloud Storage
bucket_name = os.getenv("BUCKET_NAME")
# Bucket folder from Google Cloud Storage where raw data is stored
bucket_folder_origin = os.getenv("BUCKET_FOLDER_ORIGIN")
# Credentials from GCP
credentials_json = os.getenv("CREDENTIALS")
# Set chunk size to 5MB
storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB
storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB


def log_in_gcp_clients() -> None:
    """Log in to the BigQuery and GCP clients and store them in global variables.
    """
    # Log in to the BigQuery API
    global bq_client, gcs_client
    bq_client = bigquery.Client(project_id, credentials_json)

    # Log in the GCP bucket
    gcs_client = storage.Client(project_id, credentials_json,)
    print("Logged in to GCP BigQuery and GCS clients")


def list_blobs(bucket_name: str, folder_name: str) -> list:
    """List all the blobs in a bucket and folder from Google Cloud Storage.

    Args:
    bucket_name (str): The name of the bucket in Google Cloud Storage.
    folder_name (str): The name of the folder in the bucket.

    Returns:
    list: A list with the blobs in the folder.
    """
    # Get the bucket from Google Cloud Storage
    bucket = gcs_client.get_bucket(bucket_name)
    # List all the blobs in the folder
    blobs = list(bucket.list_blobs(prefix=folder_name))
    return blobs


def read_json_to_dataframe()-> pd.DataFrame:
    """This function will read the json file from the raw data folder in
    the Google Cloud Storage bucket, create the dataframes and returns it.

    Returns:
        pd.DataFrame: A pandas dataframe with the data from the json file.
    """
    log_in_gcp_clients()
    # List all the blobs in the raw data folder
    blobs = list_blobs(bucket_name, bucket_folder_origin)
    print("BLOBS LISTED! ----------------------")
    print(blobs)
    for blob in blobs:
        # Get the name of the file
        print("The file name is "+os.path.basename(blob.name))
        file_name = os.path.basename(blob.name).split(".")[0]
        # Create the dataframe from the raw data
        # Read the json file from the blob in bucket
        # If the file name is not empty
        if file_name != "":
            print("READING FILE! ----------------------")
            # Read the json file from the blob in bucket
            df = pd.read_json(f"gs://{bucket_name}/{blob.name}", lines=True)
            print(df.info())
            print("FILE READED! ----------------------")
            return df

if __name__ == "__main__":
    read_json_to_dataframe()
    