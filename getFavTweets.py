import sys
import requests
import json
import csv
from requests_oauthlib import OAuth1

CONSUMER_KEY = '9a5vk4s0OIhqvaNAA48cG7PAT'
CONSUMER_SECRET = 'yTWGaLVyVcu6ZF9oUJ9nt4d1niTNvieCB5DNznJ7OfKMQNC4uG'
ACCESS_TOKEN = '61705925-H70JXuNOnKL7TuiZu3pI3O1K9Qe1m4RldFZhuxGqr'
ACCESS_TOKEN_SECRET = 'j9O1RUtSQI0sTSFnNv90YeEXholdArvb5vmTNoqmBTbVd'

url = "https://api.twitter.com/1.1/favorites/list.json"


screen_name="trishtrashers"

id = "screen_name="+screen_name

furl = url + "?count=200&"+id


print furl
auth = OAuth1(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)


# print auth

response = requests.get(furl,auth=auth)
parsed = json.loads(response.content)
#print json.dumps(parsed,indent=4,sort_keys=True)


#print type(parsed)
#print parsed[1]['text']


print len(parsed)

if len(parsed) == 1:
	print parsed[0]
	exit()

allFavs = []



for tweet in parsed:
	#print type(tweet['text'].encode('ascii','ignore'))
	#print tweet['id']
	try:
		xyz = tweet['text'].encode('ascii','ignore')
		allFavs.insert(0,str(xyz))
	except:
		print "Skip"


print parsed[-1]['id']
max_id = parsed[-1]['id'] - 1 



while 'true':

	furl = url + "?count=200&max_id="+str(max_id)+"&"+id
	print furl

# print auth

	response = requests.get(furl,auth=auth)
	parsed = json.loads(response.content)
	#print json.dumps(parsed,indent=4,sort_keys=True)


	#print type(parsed)
	#print parsed[1]['text']


	print len(parsed)

	if len(parsed) < 10:
		break;

	# No more likes


	for tweet in parsed:
		#print type(tweet['text'].encode('ascii','ignore'))
		#print tweet['id']
		try:
			xyz = tweet['text'].encode('ascii','ignore')
			allFavs.insert(0,str(xyz))
		except:
			print "Skip"


	max_id = parsed[-1]['id'] - 1
	print "Got 200 more likes"
	print str(len(allFavs))+" Len of allFav"
	if len(allFavs) >1500 :
		break



print "out here"
finalList = []
for tweet in allFavs:
	a = []
	a.insert(0,tweet)	
	finalList.insert(0,a)





with open('%s/%s_fav_tweets.csv' % (screen_name,screen_name), 'a+') as f:
	writer = csv.writer(f)
	writer.writerows(finalList)








