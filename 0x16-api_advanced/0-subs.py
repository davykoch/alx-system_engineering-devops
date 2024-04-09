#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit.
If an invalid subreddit is given, the function returns 0.
"""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
    Returns the number of subscribers for a given subreddit.
    '''

    user_agent = {'User-Agent': 'Lizzie'}

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data.get('data').get('subscribers')
            return subscribers
        except Exception:
            return 0
    else:
        return 0


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = argv[1]
        print(number_of_subscribers(subreddit))
