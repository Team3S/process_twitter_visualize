#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:31:10 2016

@author: selva
"""

import argparse
import json
import sys
import os
from TwitterModule import TwitterModule
from twython import Twython

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']

def parse_args():
    """
    Parse arguments Method
    :return:
    """
    parser = argparse.ArgumentParser(description='<usage> python main.py -k <KEYWORD>')
    parser.add_argument('--keyword', '-k', action='store', default='purch',
                        help='<usage> python main.py -k <KEYWORD>')
    parser.add_argument('--no', '-n', action='store', default='100',
                        help='<usage> python main.py -n <NUMBER_OF_TWEETS>')
    arguments, _ = parser.parse_known_args()
    return arguments


def check(keyword, no_of_tweets=0):
    """
    Method check tweets
    :param keyword: 
    :param no_of_tweets: 
    :return: 
    """
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    twitter = Twython(CONSUMER_KEY, access_token=ACCESS_TOKEN)
    tweets = []
    for status in twitter.search(q='\"{}\"'.format(keyword))['statuses']:
        if len(tweets) < no_of_tweets:
            text = status['text'].encode('utf-8')
            tweets.append(text)
    twitter_module = TwitterModule()
    twitter_module.prepare_corpus(tweets)


if __name__ == '__main__':
    # with open("variables.ini","r") as json_file:
    #     json_object=json.load(json_file)
    CONSUMER_KEY=os.environ['CONSUMER_KEY']
    CONSUMER_SECRET=os.environ['CONSUMER_SECRET']
    args = parse_args()
    keyword = args.keyword
    no_of_tweets=int(args.no)
    check(keyword,no_of_tweets)
