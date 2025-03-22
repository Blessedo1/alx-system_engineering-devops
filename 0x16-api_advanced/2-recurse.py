#!/usr/bin/python3
"""Contains recurse function"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches all hot article titles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom"}
    param = {"limit": 100, "after": after}

    r = requests.get(url, headers=headers, params=param, allow_redirects=False)

    if r.status_code != 200:
        return None

    data = r.json()
    posts = data.get("data", {}).get("children", [])
    after = data.get("data", {}).get("after")

    hot_list.extend(post["data"]["title"] for post in posts)

    if after:
        return recurse(subreddit, hot_list, after)

    return hot_list
