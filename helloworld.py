#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 

CONSUMER_KEY = 'ykefwUhdv17tQbEtZoc9TTxSW'
CONSUMER_SECRET = 'Nnur5btiXyxp6IL4fC2eUAzPF19gOEHX5IdYpWsXv00qcKGCgr'
ACCESS_KEY = '2903733235-o9onGdfEaluiZO4j0q3THsvqot6qJukLqTdvQTs'
ACCESS_SECRET = 'XShvoYUL0qVh7pFyZwua6nFosX4XEpE33sbsqR3rEUVeG'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes