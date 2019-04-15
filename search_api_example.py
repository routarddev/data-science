#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:15:44 2019

@author: routarddev
"""

import json
from TwitterAPI import TwitterAPI


with open("twitter_credentials.json", "r") as file:  
    credentials = json.load(file)

api = TwitterAPI(credentials['CONSUMER_KEY'], 
                 credentials['CONSUMER_SECRET'], 
                 credentials['ACCESS_TOKEN'], 
                 credentials['ACCESS_SECRET'])

r = api.request('tweets/search/30day/:env_name', {'query' : 'catalunya lang:es', 'maxResults' : '10'})

for item in r:
     print(item['text'])