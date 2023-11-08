#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    h = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}

    response = requests.get(url, headers=h, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    elif response.status_code == 404:
        return 0
