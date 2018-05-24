import sys
import os
import tweepy
import csv
import requests
import json
import re
from requests_oauthlib import OAuth1

screen_name = sys.argv[1]
if not os.path.exists(screen_name):
    os.makedirs(screen_name)
#Twitter API credentials
consumer_key = '9a5vk4s0OIhqvaNAA48cG7PAT'
consumer_secret ='yTWGaLVyVcu6ZF9oUJ9nt4d1niTNvieCB5DNznJ7OfKMQNC4uG'
access_key = '61705925-H70JXuNOnKL7TuiZu3pI3O1K9Qe1m4RldFZhuxGqr'
access_secret = 'j9O1RUtSQI0sTSFnNv90YeEXholdArvb5vmTNoqmBTbVd'





# Get all the tweets

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
		print ("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print ("...%s tweets downloaded so far" % (len(alltweets)))



	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"),tweet.entities,tweet.retweet_count,tweet.favorite_count,tweet.in_reply_to_screen_name,tweet.lang] for tweet in alltweets]

	#write the csv
	with open('%s/%s_tweets.csv' % (screen_name,screen_name), 'w',encoding='utf-8',newline='') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text","entities","retweet_count","favorites_count","in_reply_to_screen_name","lang"])
		writer.writerows(outtweets)



get_all_tweets(screen_name)



print ("Done: Get all tweets")




## Calculate user mentions

i = 0
cnt = 0


dictM = {}

with open('%s/%s_tweets.csv' % (screen_name,screen_name),'r',encoding='utf-8',newline='') as g:
    reader = csv.reader(g)
    for row in reader:
        if i >= 1:
            entity = eval(row[3])
            mentions = entity['user_mentions']
            for m in mentions:
                uname = m['screen_name']
                if uname in dictM:
                    dictM[uname] += 1
                else:
                    dictM[uname] = 1
        i = i + 1
    for i in dictM.items():
        print (i)
    a = max(dictM,key=dictM.get)
    print (a + " - " + str(dictM[a]))

    dictMList = dictM.items();

    with open('%s/%s_mentions_count.csv' % (screen_name,screen_name), 'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f)	
        writer.writerow(["Name","Count"])
        writer.writerows(dictMList)


print ("Done: Calculate User Mentions")




## Get Retweets


c = []
with open('%s/%s_retweets.csv' % (screen_name,screen_name), 'w',encoding='utf-8',newline='') as f:
	writer = csv.writer(f)

	writer.writerow(["id","created_at","text","entities","retweet_count","favorites_count","in_reply_to_screen_name","lang"])



with open('%s/%s_tweets.csv' %  (screen_name,screen_name),'r',encoding='utf-8',newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		a = row[2].startswith("RT")
		if a:
			print (a)
			with open('%s/%s_retweets.csv' % (screen_name,screen_name), 'a+',encoding='utf-8',newline='') as g:
				writer = csv.writer(g)
				writer.writerow(row)


print ("Done: Get Retweets")



## Get Hashtag Count


c = 0
dictM = {}
i=1
with open('%s/%s_tweets.csv' %  (screen_name,screen_name),'r',encoding='utf-8',newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		if i>1:
			entity = eval(row[3])
			tags = entity['hashtags']
			for m in tags:
				utag = m['text']
				if utag in dictM:
					dictM[utag] += 1
				else:
					dictM[utag] = 1	
		i = i+1
#for i in dictM.items():
#	print (i)

try:
	a = max(dictM,key=dictM.get)
	print (a + " - " + str(dictM[a]))

	dictMList = dictM.items();

	with open('%s/%s_hashtag_count.csv' % (screen_name,screen_name), 'w',encoding='utf-8',newline='') as f:
		writer = csv.writer(f)
		writer.writerow(["Tag","Count"])
		writer.writerows(dictMList)
		print ("Done: Get HashTags")

except ValueError:
	print("No hashtags")	






























