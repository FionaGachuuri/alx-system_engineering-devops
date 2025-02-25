#!/usr/bin/python3
"""
Queries the Reddit API recursively, parses titles of hot articles,
and counts occurrences of given keywords.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursively count occurrences of words in hot post titles of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditAPI/0.0.1"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    posts = data.get('children', [])

    # Normalize word_list (case-insensitive)
    word_list = [word.lower() for word in word_list]

    # Count occurrences in titles
    for post in posts:
        title_words = post['data']['title'].lower().split()
        for word in word_list:
            word_count[word] = word_count.get(word, 0) + title_words.count(word)

    # Pagination handling
    after = data.get('after')
    if after:
        return count_words(subreddit, word_list, after, word_count)

    # Sorting: first by count (descending), then alphabetically (ascending)
    sorted_counts = sorted(
        [(word, count) for word, count in word_count.items() if count > 0],
        key=lambda x: (-x[1], x[0])
    )

    # Print results
    for word, count in sorted_counts:
        print(f"{word}: {count}")
