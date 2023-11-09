#!/usr/bin/python3
"""queries the Reddit API recursively."""
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """Queries the Reddit API parses the title of
    all hot article"""

    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        sorted_word = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word:
            if count > 0:
                print('{}: {}'.format(word, count))
        return

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    parameters = {'limit': 100, 'after': after}
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            words = re.findall(r'\b\w+\b', title.lower())

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return

    count_words(subreddit, word_list, aft, word_dict)
