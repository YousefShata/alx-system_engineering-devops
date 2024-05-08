#!/usr/bin/python3
"""
0-main
"""
import requests


def number_of_subscribers(subreddit):
    """
    getting number of subs
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
 
    headers = {
        "User-Agent": "MyRedditApp/1.0 by MyShata"
    }

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    
    return 0
