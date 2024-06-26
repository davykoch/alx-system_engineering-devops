#!/usr/bin/python3
"""Queries the Reddit API and returns the number
of subscribers for a given subreddit."""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    headers = {'User-Agent': 'koechdavis24@gmail.com'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=headers).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(argv[1])
        if subscribers == 0:
            print("OK")
        else:
            print(subscribers)
