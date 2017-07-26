#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from twython import Twython
APP_KEY = '73611129-OfrRLD6v4DweNTuJHCqD8vygilgv2fHXLZoOIBcNH'
APP_SECRET = 'YmJ8734LQtJtSV21RqDpM0OzsQJeipPMcDtdaHzeSsz3D'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
