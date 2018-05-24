import requests
import json
import csv
from requests_oauthlib import OAuth1

CONSUMER_KEY = '9a5vk4s0OIhqvaNAA48cG7PAT'
CONSUMER_SECRET = 'yTWGaLVyVcu6ZF9oUJ9nt4d1niTNvieCB5DNznJ7OfKMQNC4uG'
ACCESS_TOKEN = '61705925-H70JXuNOnKL7TuiZu3pI3O1K9Qe1m4RldFZhuxGqr'
ACCESS_TOKEN_SECRET = 'j9O1RUtSQI0sTSFnNv90YeEXholdArvb5vmTNoqmBTbVd'

url = "https://api.twitter.com/1.1/favorites/list.json"


screen_name="ikamalhaasan"

id = "screen_name="+screen_name

furl = url + "?"+id


print furl
auth = OAuth1(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)


# print auth

response = requests.get(furl,auth=auth)
parsed = json.loads(response.content)
#print json.dumps(parsed,indent=4,sort_keys=True)


#print type(parsed)
#print parsed[1]['text']

allFavs = []



for tweet in parsed:
	#print type(tweet['text'].encode('ascii','ignore'))
	allFavs.insert(0,tweet['text'].encode('ascii','ignore'))



finalList = []
for tweet in allFavs:
	a = []
	a.insert(0,tweet)	
	finalList.insert(0,a)





with open('%s_fav_tweets.csv' % screen_name, 'wb') as f:
	writer = csv.writer(f)
	writer.writerows(finalList)






