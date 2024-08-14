#!/usr/bin/python3
""" Get Reddit Subscribers """
import requests

def number_of_subscribers(subreddit):
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyCoolReqName/1.0 (by /u/ReplyAdventurous5909)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
