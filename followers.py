import tweepy
import sys

auth = tweepy.OAuthHandler('9a5vk4s0OIhqvaNAA48cG7PAT', 'yTWGaLVyVcu6ZF9oUJ9nt4d1niTNvieCB5DNznJ7OfKMQNC4uG')
auth.set_access_token('61705925-H70JXuNOnKL7TuiZu3pI3O1K9Qe1m4RldFZhuxGqr', 'j9O1RUtSQI0sTSFnNv90YeEXholdArvb5vmTNoqmBTbVd')

api = tweepy.API(auth)


for user in tweepy.Cursor(api.followers, screen_name="akshaykumar",count=50).items():
    print ("%s %d",user.screen_name, user.followers_count)