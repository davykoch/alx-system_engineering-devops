#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count occurrences
        in the titles.
        after (str): A token indicating the starting point for the
        next page of
        results. Default is None.
        counts (dict): A dictionary to store counts of keywords.
        Default is None.

    Returns:
        None
    """
    if counts is None:
        counts = {}

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
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
            return

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if title.count(word.lower()) > 0:
                    counts[word.lower()] = counts.get(word.lower(), 0) + \
                        title.count(word.lower())

        after = data["data"]["after"]
        count_words(subreddit, word_list, after, counts)
    else:
        print("None")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'"
              .format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
