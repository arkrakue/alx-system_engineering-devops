#!/usr/bin/python3
"""Get the total subcriber count"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the
    number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'subscriber_count'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json()
    return data['data']['subscribers']
