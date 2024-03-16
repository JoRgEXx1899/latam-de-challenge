from typing import List, Tuple
from collections import defaultdict
import ujson as json
import emoji


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """This function will read the json line by line and iterate through the 
    'content' column to find the top 10 emojis and their frequency in the tweets.
    Works by using dictionary to count the emojis and emoji library to extract 
    the emojis from the tweet content .

    Args:
        file_path (str): file path to the json file in local file system. 

    Returns:
        List[Tuple[str, int]]: Top 10 emojis and their frequency in the tweets.
    """
    # Create a dictionary to count emojis by date
    emoji_count = defaultdict(int)
    # Open file in read mode
    file = open(file_path, "r")
    # Iterate over each line in the file
    for line in file:
        # Load each line as a JSON object
        tweet = json.loads(line)
        # Get the content of the tweet or an empty string if there is no content
        contenido = tweet.get('content', '')
        # Extract the emojis from the tweet content and update the emoji counter
        emojis_in_tweet = [emoticon['emoji']
                           for emoticon in emoji.emoji_list(contenido)]
        for emojii in emojis_in_tweet:
            emoji_count[emojii] += 1
    # Sort the dictionary by value in descending order
    result = sorted(
        emoji_count.items(), key=lambda x: x[1], reverse=True)[:10]

    return result
