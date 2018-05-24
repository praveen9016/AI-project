import re
import csv
with open('Elli_Eats/Elli_Eats_tweets_alone.csv','rb') as f:
	reader = csv.reader(f,delimiter=',')
	for row in reader:
		a = row[0].startswith("RT")
		print a
		c = []
		if a:
			c.append(row[0])
			with open('Elli_Eats/Elli_Eats_retweets.csv', 'a+') as f:
				writer = csv.writer(f)
				writer.writerow(c)
