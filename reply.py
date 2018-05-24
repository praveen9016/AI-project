#!/usr/bin/env python
import tweepy

 
CONSUMER_KEY = 'ykefwUhdv17tQbEtZoc9TTxSW'
CONSUMER_SECRET = 'Nnur5btiXyxp6IL4fC2eUAzPF19gOEHX5IdYpWsXv00qcKGCgr'
ACCESS_KEY = '2903733235-o9onGdfEaluiZO4j0q3THsvqot6qJukLqTdvQTs'
ACCESS_SECRET = 'XShvoYUL0qVh7pFyZwua6nFosX4XEpE33sbsqR3rEUVeG'
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
twt = api.search(q="Hello World!")     
 
#list of specific strings we want to check for in Tweets
t = ['Hello world!',
    'Hello World!',
    'Hello World!!!',
    'Hello world!!!',
    'Hello, world!',
    'Hello, World!']
 
for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)