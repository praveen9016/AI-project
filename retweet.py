#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Twitter Bot Retweet version
Copyright 2013, Verri Andriawan, didesignin.com 
http://didesignin.com/
'''

from time import sleep
from sys import exit, path
from datetime import datetime
import tweepy	

# Setting API
CONSUMER_KEY = 'ykefwUhdv17tQbEtZoc9TTxSW'
CONSUMER_SECRET = 'Nnur5btiXyxp6IL4fC2eUAzPF19gOEHX5IdYpWsXv00qcKGCgr'
ACCESS_KEY = '2903733235-o9onGdfEaluiZO4j0q3THsvqot6qJukLqTdvQTs'
ACCESS_SECRET = 'XShvoYUL0qVh7pFyZwua6nFosX4XEpE33sbsqR3rEUVeG'
USERNAME = 'pravo9016' 

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Serve Stack
old_stack = []

try:
	while True:
		# GET 20 Mentions
		ment = api.mentions_timeline()
		new_stack = []

		if(len(old_stack) > 0) :
			for stat in ment:
				new_stack.append(stat.id)
				if(stat.id in old_stack):
					break
				else:
					if(stat.user.screen_name != USERNAME):
						api.retweet(stat.id)
						print ('retweet : '+stat.text+' from '+stat.user.screen_name)
					sleep(5)
			old_stack = new_stack
			
		else : 
			for stat in ment:
				new_stack.append(stat.id)
				if(stat.user.screen_name != USERNAME):
					api.retweet(stat.id)
				sleep(5)
			old_stack = new_stack
		sleep(5*60) # will update every 5 minutes

except KeyboardInterrupt:
	exit()