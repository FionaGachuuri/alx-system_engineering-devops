#!/usr/bin/python3
"""
Queries the Reddit API recursively to get all hot post titles of a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch titles of all hot articles for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditAPI/0.0.1"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    posts = data.get('children', [])

    for post in posts:
        hot_list.append(post['data']['title'])

    after = data.get('after')
    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
