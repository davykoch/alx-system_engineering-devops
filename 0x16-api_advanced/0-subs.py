#!/usr/bin/python3
"""Queries the Reddit API and returns the number
of subscribers for a given subreddit."""

import requests
from sys import argv


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    headers = {'User-Agent': 'YourCustomUserAgent/1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.exceptions.HTTPError:
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subscribers = number_of_subscribers(argv[1])
        print(subscribers)
