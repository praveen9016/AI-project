import tweepy

CONSUMER_KEY = '9a5vk4s0OIhqvaNAA48cG7PAT'
CONSUMER_SECRET = 'yTWGaLVyVcu6ZF9oUJ9nt4d1niTNvieCB5DNznJ7OfKMQNC4uG'
ACCESS_TOKEN = '61705925-H70JXuNOnKL7TuiZu3pI3O1K9Qe1m4RldFZhuxGqr'
ACCESS_TOKEN_SECRET = 'j9O1RUtSQI0sTSFnNv90YeEXholdArvb5vmTNoqmBTbVd'


#OAuth
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = "Status Update made using Tweepy :D"
api.update_status(status=status)
