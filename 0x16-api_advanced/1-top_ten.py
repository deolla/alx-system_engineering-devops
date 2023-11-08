#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    try:
        response = requests.get(url, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print(None)
        return

    data = response.json()

    if "data" not in data:
        print(None)
        return
    for post in data["data"]["children"][:10]:
        print(post["data"]["title"])
