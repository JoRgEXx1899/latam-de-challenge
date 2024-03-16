from typing import List, Tuple
from collections import defaultdict
import re

import ujson as json


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """This function will read the json or parquet file with pandas and iterate 
    through the 'content' column to find the mentions (@) in each tweet. Returns 
    top 10 mentioned users and their frequency.

    Args:
        file_path (str): file path to the json file or parquet file in local file system. 
        Also, it can be a file path to the file in the Google Cloud Storage bucket.

    Returns:
        List[Tuple[str, int]]: Top 10 mentioned users and their frequency in the tweets.
    """
    # Create a dictionary to count emojis by date
    mentioned_users_count = defaultdict(int)
    # Open file in read mode
    file = open(file_path, "r")
    # Iterate over each line in the file
    for line in file:
        # Load each line as a JSON object
        tweet = json.loads(line)
        # Get the content of the tweet or an empty string if there is no content
        content = tweet.get('content', '')
        # Extract all the mentions r'@(\w+)' from content
        mentions_in_tweet = [
            mention for mention in re.findall(r'@(\w+)', content)]
        for mention in mentions_in_tweet:
            mentioned_users_count[mention] += 1
    # Sort the dictionary by value in descending order
    top_10_users = sorted(mentioned_users_count.items(),
                          key=lambda x: x[1], reverse=True)[:10]
    return top_10_users
