#!/usr/bin/python3
"""this api requests for the top ten hot posts"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'popular_api_hot'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data['data']['children']

    for post in posts:
        print(post['data']['title'])
