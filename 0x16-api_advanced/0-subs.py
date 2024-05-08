#!/usr/bin/python3
"""
0-main
"""
import requests
import json


def number_of_subscribers(subreddit):
    """
    getting number of subs
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        return res.json()['data']['subscribers']

    return 0
