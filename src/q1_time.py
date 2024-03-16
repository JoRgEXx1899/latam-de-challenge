from typing import List, Tuple
from datetime import datetime

import pandas as pd


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """This function will read the json or parquet file with pandas. Date is 
    converted to a date object and the user_name of user is used as user 
    key. Then rows are counted through the 'dates' column to find the top 10 
    dates with more tweets. Then the user with more tweets on each date is
    determined by the count of tweets on each date.
    
    Args:
        file_path (str): file path to the json file or parquet file in local 
        file system. Also, it can be a file path to the file in the Google Cloud 
        Storage bucket.
    Returns:
        List[Tuple[str, int]]: Top 10 dates of tweets and user with more 
        tweets per day.
    """
    # Read the json file from the blob in bucket
    if file_path.endswith(".json"):
        df = pd.read_json(file_path, lines=True)
    elif file_path.endswith(".parquet"):
        df = pd.read_parquet(file_path)
    # Convert the date column from datetime to format date
    df["date"] = df["date"].dt.date
    # Get the user and print for the first row
    # User is a nested json, so we need to unnest it. We just need username from user
    # Set the user column as a username nested in user
    df["user"] = df["user"].apply(lambda x: x["username"])
    # The top 10 dates where there are the most tweets. Mention the user
    # (username) who has the most publications for each of those days
    top_10_dates = df["date"].value_counts().head(10)
    # from the top 10 dates, get the user with the most tweets in each date
    # Define a list to store the result
    result = []
    # Iterate over the top 10 dates
    for date in top_10_dates.index:
        # Get the user with the most tweets in the date
        user = df[df["date"] == date]["user"].value_counts().idxmax()
        # Append the date and the user to the result list
        result.append((date, user))
    return result
