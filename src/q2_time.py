from typing import List, Tuple
import pandas as pd
import emoji

from collections import Counter


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """This function will read the json or parquet file with pandas and iterate 
    through the 'content' column to find the top 10 emojis and their frequency 
    in the tweets.

    Args:
        file_path (str): file path to the json file or parquet file in local file system. 
        Also, it can be a file path to the file in the Google Cloud Storage bucket.

    Returns:
        List[Tuple[str, int]]: Top 10 emojis and their frequency in the tweets.
    """
    # Read the json file from the blob in bucket
    if file_path.endswith(".json"):
        df = pd.read_json(file_path, lines=True)
    elif file_path.endswith(".parquet"):
        df = pd.read_parquet(file_path)

    # Creates an empty list to store all the emojis in the tweets contents
    emoji_list = []

    # Iterates through the 'content' column of the DataFrame
    for content in df['content']:
        # Extract the emojis from each content using the emoji package
        emojis_in_tweet = [
            emoticon['emoji'] for emoticon in emoji.emoji_list(content)
        ]
        # Append the emojis to the list
        emoji_list.extend(emojis_in_tweet)

    # Count the frequency of each emoji in the list
    #emoji_freq = {emoji: emoji_list.count(emoji) for emoji in emoji_list}
    emoji_freq = Counter(emoji_list)
    # Sort the dictionary by value in descending order
    sorted_emoji_freq = sorted(
        emoji_freq.items(), key=lambda x: x[1], reverse=True)[:10]
    return sorted_emoji_freq
