#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Print the title of the  10 hotest post on a given  subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {"User-Agent": "custom_user_agent"}
    params = {
        "limit": 10
              }
    responds = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if responds.status_code == 200:

        data = responds.json().get("data")
        return [
            print(c.get("data").get("title")) for c in data.get("children")
            ]
    else:
        return print("None")