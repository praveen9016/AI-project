import re
import csv
with open('Elli_Eats/Elli_Eats_tweets_alone.csv','rb') as f:
	reader = csv.reader(f,delimiter=',')
	for row in reader:
		a = re.findall(r"#(\w+)",row[0])
		print a
		if a:
			with open('Elli_Eats/Elli_Eats_hashtags.csv', 'a+') as f:
				writer = csv.writer(f)

				for c in a:
					d = []
					d.append(c)
					writer.writerow(d)
