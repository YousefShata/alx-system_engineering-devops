#!/usr/bin/python3
"""
recurse model
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Function Docs
    """

    reddit = "https://www.reddit.com"
    url = "{}/r/{}/hot/.json?sort={}&limit={}&count={}&after={}".format(
            reddit, subreddit, "hot", 30, count, after)

    headers = {
        "User-Agent": "MyRedditApp/1.0 by Shata"
    }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()['data']['children']
        hot_list.extend(list(map(lambda x: x['data']['title'], posts)))
        if len(posts) >= 30 and response.json()['data']['after']:
            return recurse(subreddit, hot_list,
                           count + len(posts),
                           response.json()['data']['after']
                           )
        else:
            return hot_list if hot_list else None
    else:
        return hot_list if hot_list else None
