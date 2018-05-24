import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "6uVOqNbitF3iaLTvolXp3RRhW"
consumer_secret = "ezbjUtyaSvrOQbg7zwLi7aELFfwMjVh1J6TpLQnuTLHMXiyQLC"
access_key = "443560601-WRmPXHqJVZa50a6sZi55RwuC5unZF8UOCvj02zyI"
access_secret = "O9p47u8xdch96ES3C8oST4GS07DlVlPqITqc9FsompN9b"

id_list = ['612614614543524000','609196317466694000']

def get_retweet_count(tweet_id):
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    tweet = api.get_status(tweet_id)
    return tweet

for id in id_list:
   print get_retweet_count(id), id
