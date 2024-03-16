from typing import List, Tuple
import pandas as pd
import re

from collections import Counter


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """This function will read the json or parquet file with pandas and iterate 
    through the 'content' column to find the mentions (@) in each tweet. Returns 
    top 10 mentioned users and their frequency.

    Args:
        file_path (str): file path to the json file or parquet file in local file system. 
        Also, it can be a file path to the file in the Google Cloud Storage bucket.

    Returns:
        List[Tuple[str, int]]: Top 10 mentioned users and their frequency in the tweets.
    """
    # Read the json file from the blob in bucket
    if file_path.endswith(".json"):
        df = pd.read_json(file_path, lines=True)
    elif file_path.endswith(".parquet"):
        df = pd.read_parquet(file_path)

    # Creates an empty list to store all the mentioned users in the tweets contents
    mentioned_user_list = []
    # Iterates through the 'content' column of the DataFrame
    for content in df['content']:
        # Extract all the mentions r'@(\w+)' from content
        mentions_in_tweet = [
            mention for mention in re.findall(r'@(\w+)', content)
        ]
        # Append the user to the mentioned users list
        mentioned_user_list.extend(mentions_in_tweet)
    
    # Count the frequency of each mentioned user in the list
    user_freq = Counter(mentioned_user_list)
    top_10_users=sorted(
        user_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_10_users
