import tweepy
SCREEN_NAME1 = 'NimratOfficial'
SCREEN_NAME2 = 'akshaykumar'
CONSUMER_KEY = '9a5vk4s0OIhqvaNAA48cG7PAT'
CONSUMER_SECRET ='yTWGaLVyVcu6ZF9oUJ9nt4d1niTNvieCB5DNznJ7OfKMQNC4uG'
ACCESS_TOKEN = '61705925-H70JXuNOnKL7TuiZu3pI3O1K9Qe1m4RldFZhuxGqr'
ACCESS_TOKEN_SECRET = 'j9O1RUtSQI0sTSFnNv90YeEXholdArvb5vmTNoqmBTbVd'
followercount=0
followingcount=0 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
    
follow = api.followers_ids(SCREEN_NAME2)
friend = api.friends_ids(SCREEN_NAME2)
	
followers = api.followers_ids(SCREEN_NAME1)
friends = api.friends_ids(SCREEN_NAME1)

for f in followers:
    if f in friend:
        print ("User : {0}?".format(api.get_user(f).screen_name))
        		
			
