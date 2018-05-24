import tweepy
SCREEN_NAME = 'pravo9016'
CONSUMER_KEY = '9a5vk4s0OIhqvaNAA48cG7PAT'
CONSUMER_SECRET ='yTWGaLVyVcu6ZF9oUJ9nt4d1niTNvieCB5DNznJ7OfKMQNC4uG'
ACCESS_TOKEN = '61705925-H70JXuNOnKL7TuiZu3pI3O1K9Qe1m4RldFZhuxGqr'
ACCESS_TOKEN_SECRET = 'j9O1RUtSQI0sTSFnNv90YeEXholdArvb5vmTNoqmBTbVd'
followercount=0
followingcount=0 
flrcount=0
flwcount=0
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
    
followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

for s in followers:
  followercount=followercount+1
for d in friends:
  followingcount=followingcount+1

print('\n')
print( "Followers:",followercount)
print( "Following:",followingcount)
print('\n')

for f in friends:
    if f not in followers:
        print ("Unfollow {0}?".format(api.get_user(f).screen_name))
        if input("Y/N?") == 'y' or 'Y':
            api.destroy_friendship(f);     	
			
for s in followers:
  flrcount=flrcount+1
for d in friends:
  flwcount=flwcount+1

print('\n')
print( "Followers:",flrcount)
print( "Following:",flwcount)
print('\n')