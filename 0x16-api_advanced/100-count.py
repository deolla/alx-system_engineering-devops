#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, counter={}, after="", count=0):
    """Prints counts of words found in hot posts of given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)'}
    params = {'after': after, 'count': count, 'limit': 100}

    response = requests.get(url, headers=h, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for m in results.get("children"):
        title = m.get("data").get("title").lower().split()
        for l in word_list:
            if l.lower() in title:
                times = len([t for t in title if t == l.lower()])
                if counter.get(l) is None:
                    counter[l] = times
                else:
                    counter[l] += times

    if after is None:
        if len(counter) == 0:
            print("")
            return
        counter = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in counter]
    else:
        count_words(subreddit, word_list, counter, after, count)
