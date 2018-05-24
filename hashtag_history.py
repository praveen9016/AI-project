import csv

new_tweet_hashtags = ['travel', 'Africa','WTM2012']
htags = []
count = 0


with open('Elli_Eats/Elli_Eats_hashtags.csv') as g:
	reader = csv.reader(g)
	for row in reader:
		htags.append(row[0])
print htags
for tag in new_tweet_hashtags:
	if tag in htags:
		print tag
		count = count + htags.count(tag)

ttlhtags = len(htags)
score = 0
if count == 0:
	score = 0
elif count >= 1 and count <= 3:
	score = 0.2
elif count >=4 and count <= 6:
	score = 0.4
elif count >= 7:
	score = 0.7

print "hashtag history score",score
	
