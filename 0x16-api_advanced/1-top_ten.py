#!/usr/bin/python3
"""
0-main
"""
import requests


def top_ten(subreddit):
    """
    get top 10
    """

    url = "https://www.reddit.com/r/{}/hot/.json ?sort={}&limit={}".format(
        subreddit, "top", 10)

    headers = {
        "User-Agent": "MyRedditApp/1.0 by Shata"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])

    print("None")
