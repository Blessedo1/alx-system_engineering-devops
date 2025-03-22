#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/aabout.json".format(subreddit)
    headers = {"User-Agent": "Custom"}

    r = requests.get(url, headers=headers, allow_redirects=False)

    if r.status_code == 200:
        data == r.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0
