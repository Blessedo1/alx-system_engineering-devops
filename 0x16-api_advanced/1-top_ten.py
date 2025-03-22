#!/usr/bin/python3
"""Contains top_ten function"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "custom"}
    param = {"limit": 10}

    r = requests.get(url, headers=headers, params=param, allow_redirects=False)

    if r.status_code == 200:
        data = r.json()
        posts = data.get("data", {}).get("children", 0)
        for i in posts:
            print(i["data"]["title"])
    else:
        print(None)
