#!/usr/bin/python3
"""Reddit API for top 10 of subreddit"""
import requests


def top_ten(subreddit):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh;' +
               ' Intel Mac OS X 10_10_1) AppleWebKit/537.36 ' +
               '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    http = requests.get('https://www.reddit.com/r/{}/hot.json'
                        .format(subreddit), params={'limit': 10},
                        headers=headers, allow_redirects=False)

    if http.status_code == 404:
        print(None)
    else:
        http = http.json()
        lists = [v for k, v in http.items() if k == 'data']
        lists = lists[0].get('children')
        for l in lists:
            print(l.get('data').get('title'))
