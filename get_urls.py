import re
import csv
from ttp import ttp
p=ttp.Parser()
with open('Vajralight_tweets_alone.csv','rb') as f:
	reader = csv.reader(f,delimiter=',')
	for row in reader:
		if row[0]!='text':
			a = str(row)
			result = p.parse(a)
			u = result.urls
			us = result.users
		
			if u:
				print u						
				with open('Vajralight_urls.csv', 'a+') as s:
					writer = csv.writer(s)
					writer.writerow(u)
			if us != 'None':
				print us
				with open('Vajralight_replies.csv','a+') as d:
					writer = csv.writer(d)
					writer.writerow(us)
