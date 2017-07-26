#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import argparse
from twython import Twython
APP_KEY = 'xx'
APP_SECRET = 'xx'

def parse_args():
    """
    Parse arguments Method
    :return:
    """
    parser = argparse.ArgumentParser(description='<usage> python main.py -k <KEYWORD>')
    parser.add_argument('--keyword', '-k', action='store', default='pyspark',
                        help='<usage> python main.py -k <KEYWORD>')
    arguments, _ = parser.parse_known_args()
    return arguments


def check():

    twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
    ACCESS_TOKEN = twitter.obtain_access_token()
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    results = twitter.cursor(twitter.search, q='')
    for result in results:
        print result
        break




if __name__ == '__main__':
    args = parse_args()
    keyword = args.keyword
    print(keyword)
    check()
