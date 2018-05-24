import sys
import re
import csv
screen_name = sys.argv[1]
c = 0
dictM = {}
i=1
with open('Dataset/%s/%s_tweets.csv' %  (screen_name,screen_name),'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		if i>1:
			print row[3]
			entity = eval(row[3])
			tags = entity['hashtags']
			for m in tags:
				utag = m['text']
				if utag in dictM:
					dictM[utag] += 1
				else:
					dictM[utag] = 1	
		i = i+1
for i in dictM.items():
	print i

try:
	a = max(dictM,key=dictM.get)
	print a + " - " + str(dictM[a])

	dictMList = dictM.items();

	with open('Dataset/%s/%s_hashtag_count.csv' % (screen_name,screen_name), 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["Tag","Count"])
		writer.writerows(dictMList)

except ValueError:
	print "No hashtags"	


