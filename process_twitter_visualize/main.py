#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import argparse
import json
from twython import Twython
CONSUMER_KEY = 'vG39KwmuObu56TmYpHk5q6niM'
CONSUMER_SECRET = 'mGxwHb3iNnsGg9P3kJKvWctPL2UjHBRWo6i9ET6wUrEVArnbSR'

def parse_args():
    """
    Parse arguments Method
    :return:
    """
    parser = argparse.ArgumentParser(description='<usage> python main.py -k <KEYWORD>')
    parser.add_argument('--keyword', '-k', action='store', default='pyspark',
                        help='<usage> python main.py -k <KEYWORD>')
    parser.add_argument('--no', '-n', action='store', default='5',
                        help='<usage> python main.py -n <NUMBER_OF_TWEETS>')
    arguments, _ = parser.parse_known_args()
    return arguments


def check(keyword,no_of_tweets=0):

    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    twitter = Twython(CONSUMER_KEY, access_token=ACCESS_TOKEN)
    tweets = []
    for status in twitter.search(q='\"{}\"'.format(keyword))['statuses']:
        if len(tweets)<no_of_tweets:
            text = status['text'].encode('utf-8')
            tweets.append(text)
    with open('tweet_search_{}.json'.format(keyword), 'w') as f:
        json.dump(tweets, f, indent=4)



if __name__ == '__main__':
    args = parse_args()
    keyword = args.keyword
    no_of_tweets=args.no
    print(keyword)
    check(keyword,no_of_tweets)
