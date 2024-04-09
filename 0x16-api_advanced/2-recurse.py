#!/usr/bin/python3
"""
Queries the Reddit API recursively and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles.
        Default is None.
        after (str): A token indicating the starting point for the
        next page of results. Default is None.

    Returns:
        list: A list containing the titles of all hot articles for the
        given subreddit, or None if no results are found.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?" \
          f"limit=100&after={after}"

    headers = {
                "User-Agent": (
                 "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                 "AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/58.0.3029.110 Safari/537.3"
                             )
              }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if not posts:
            return hot_list

        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        return recurse(subreddit, hot_list, after)
    else:
        return None


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
