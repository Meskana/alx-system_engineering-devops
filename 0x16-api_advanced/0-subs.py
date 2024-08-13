#!/usr/bin/python3
import sys
import requests
"""
 function that queries the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "custom_user_agent"}
    try:
        responds = requests.get(url, headers=headers, allow_redirects=False)
        if responds.status_code == 200:
            data = responds.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return e


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <subreddit>")
        sys.exit(1)
    subreddit = sys.argv[1]
    number_of_subscribers(subreddit)
    print(f"{number_of_subscribers(subreddit)}")
