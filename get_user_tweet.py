#!/usr/bin/env python```````````````````````````
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "6uVOqNbitF3iaLTvolXp3RRhW"
consumer_secret = "ezbjUtyaSvrOQbg7zwLi7aELFfwMjVh1J6TpLQnuTLHMXiyQLC"
access_key = "443560601-WRmPXHqJVZa50a6sZi55RwuC5unZF8UOCvj02zyI"
access_secret = "O9p47u8xdch96ES3C8oST4GS07DlVlPqITqc9FsompN9b"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.entities,tweet.retweet_count,tweet.favorite_count,tweet.in_reply_to_screen_name,tweet.lang] for tweet in alltweets]

	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text","entities","retweet_count","favorites_count","in_reply_to_screen_name","lang"])
		writer.writerows(outtweets)
	
	pass
	userdet = api.users_lookup(screen_name=screen_name)
	userdetc = [userdet.created_at, userdet.description,userdet.favourites_count,userdet.followers_count,userdet.friends_count,userdet.id_str,userdet.lang,userdet.statuses_count,userdet.verified]
	with open('%s_user_detail.csv' % screen_name,'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["created_at","description","favourites_count","followers_count","friends_count","id_str","lang","statuses_count","verified"])
		writer.writerows(userdetc)
	pass
if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("Elli_Eats")
