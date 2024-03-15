import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from google.cloud import storage

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
    """Log in to the GCP client of storage and set it in global variables.
    """
    global gcs_client
    # Log in the GCP bucket
    gcs_client = storage.Client(project_id, credentials_json,)
    print("Logged in to GCP / GCS client")


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


def get_gcs_path() -> str:
    """This function will return the path to the file in the Google Cloud 
    Storage bucket.

    Returns:
        str: A string with the path to the file in the Google Cloud Storage bucket.
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
        # Create the file path in the Google Cloud Storage bucket to the file
        # Read the json file from the blob in bucket
        # If the file name is not empty
        if file_name != "":
            print("BUILDING FILE PATH! ----------------------")
            # Build the file path in the Google Cloud Storage bucket to the file
            file_path_gcs = f"gs://{bucket_name}/{blob.name}"
            return file_path_gcs


def read_gcs_json_to_dataframe(file_path: str) -> pd.DataFrame:
    """This function will read the json file from the raw data folder in
    the Google Cloud Storage bucket, create the dataframes and returns it.

      Args:
        file_path (str): the file path to the json file in the Google Cloud Storage bucket.

    Returns:
        pd.DataFrame: A pandas dataframe with the data from the json file.

    """
    log_in_gcp_clients()
    print("READING FILE! ----------------------")
    # Read the json file from the blob in bucket
    df = pd.read_json(file_path, lines=True)
    print("FILE READED! ----------------------")
    return df


def download_file(file_path_gcs, directory_path: Path) -> Path:
    """A function which downloads the blob file into the path defined. 
    If the file already exists, it doesn't download it.
    Returns the path where the file is downloaded

    Args:
        blob (blob): A blob from GCS to download.
        directory_path (Path): A path in the project to storage files temporaly downloaded.

    Returns:
        Path: the path where the file is downloaded
    """
    # Download the file from the Google Cloud Storage bucket at the file path
    blob = storage.Blob.from_string(file_path_gcs, client=gcs_client)
    local_path = os.path.join(directory_path, os.path.basename(blob.name))
    # If the file already exists don't download it
    if not os.path.exists(local_path):
        blob.download_to_filename(local_path, checksum=None)
    return local_path


if __name__ == "__main__":
    read_gcs_json_to_dataframe()
