#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given, returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditAPI/0.0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    try:
        return response.json().get('data', {}).get('subscribers', 0)
    except ValueError:
        return 0
