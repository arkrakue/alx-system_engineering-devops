#!/usr/bin/python3
"""Count hot articles for specific title"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after="", word_count=Counter()):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if not response.status_code == 200:
        return

    data = response.json().get('data')
    after = data.get('after')
    posts = data.get('children')

    for post in posts:
        title = post.get('data').get('title').lower().split()
        for word in word_list:
            word_count[word] += title.count(word)

    if after is not None:
        count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(word_count.items(),
                                   key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_count:
            if count > 0:
                print("{}: {}".format(word, count))


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".
              format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
