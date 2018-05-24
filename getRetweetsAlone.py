import sys
import re
import csv
screen_name = "AswinMahendran"
c = []
with open('%s/%s_retweets.csv' % (screen_name,screen_name), 'wb') as f:
	writer = csv.writer(f)

	writer.writerow(["id","created_at","text","entities","retweet_count","favorites_count","in_reply_to_screen_name","lang"])



with open('%s/%s_tweets.csv' %  (screen_name,screen_name),'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		a = row[2].startswith("RT")
		if a:
			print a
			with open('%s/%s_retweets.csv' % (screen_name,screen_name), 'a+') as g:
				writer = csv.writer(g)
				writer.writerow(row)









