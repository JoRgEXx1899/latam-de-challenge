from typing import List, Tuple
from datetime import datetime
from collections import defaultdict
import ujson as json


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Create a nested dictionary to count users by date
    users_per_date = defaultdict(lambda: defaultdict(int))
    # Open file in read mode
    file = open(file_path, "r")
    # Iterate over each line in the file
    for line in file:
        # Load each line as a JSON object
        tweet = json.loads(line)
        # Extract the date of the tweet and convert it to a date object
        date_tweet_str = tweet['date'].split("T")[0]
        # Format the date as a date object
        date_tweet = datetime.strptime(date_tweet_str, '%Y-%m-%d').date()
        # Get the username of the tweet
        user_name = tweet['user']['username']
        # Add 1 to the user count at the date
        users_per_date[date_tweet][user_name] += 1
    # Initialize an empty list to store the top dates and users
    dates_main_users = []
    # Iterate through the dates and their user counts
    for date, user_count in users_per_date.items():
        # Find the user with the maximum count for each date
        main_user = max(user_count, key=user_count.get)
        # Add the date and the main user to the list
        dates_main_users.append((date, main_user))
    # Sort the list by user count in descending order and take the first 10 entries by slicing the list
    result = sorted(
        dates_main_users, key=lambda x: users_per_date[x[0]][x[1]], reverse=True)[:10]
    # sort the result by date ascending
    result.sort(key=lambda x: x[0])

    return result
