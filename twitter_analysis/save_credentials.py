#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:13:58 2019

@author: routarddev
"""

import json

credentials = {}
credentials['CONSUMER_KEY'] = 'XXX'
credentials['CONSUMER_SECRET'] = 'XXX'
credentials['ACCESS_TOKEN'] = 'XXX'
credentials['ACCESS_SECRET'] = 'XXX'

with open("twitter_credentials.json", "w") as file:
    json.dump(credentials, file)