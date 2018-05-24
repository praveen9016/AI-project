import csv
import sys
i = 0

screen_name = sys.argv[1]
with open('Dataset/%s/%s_tweets.csv' % (screen_name,screen_name),'r',encoding='utf-8',newline='') as g:
	reader = csv.reader(g)
	for row in reader:
		if i >= 1 and i<= 10:
		  print ("tweet",i)
		  fav_count = row[5]
		  print ("favorite count",fav_count)
		  fav_score = (int)(fav_count*1)
		  print ("favorite score = ",fav_score)
		  retweet_count = row[4]
		  print ("retweet count",retweet_count)
		  retweet_score = (int)(retweet_count*50)/100
		  print ("retweet score",retweet_score)
		  print (row[3].encode("utf-8"))
		i = i + 1	

	