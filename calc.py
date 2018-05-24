import csv
import sys

i = 0
cnt = 0


dictM = {}


screen_name = sys.argv[1]
with open('Dataset/%s/%s_tweets.csv' % (screen_name,screen_name)) as g:
    reader = csv.reader(g)
    for row in reader:
        if i >= 1:
            entity = eval(row[3])
            mentions = entity['user_mentions']
            for m in mentions:
                uname = m['screen_name']
                if uname in dictM:
                    dictM[uname] += 1
                else:
                    dictM[uname] = 1
        i = i + 1
    for i in dictM.items():
        print(i)
    a = max(dictM,key=dictM.get)
    print(a + " - " + str(dictM[a]))

    dictMList = dictM.items();

    with open('score2.csv' % (screen_name,screen_name), 'w',encoding='utf-8',newline='') as f:
	     writer = csv.writer(f)
	     sim=semsim*0.75+0.25*statsim
	     writer.writerow(["Name","Score1","Score2"])
	     writer.writerows(dictMList)






 




        # outtweets = [[tweet.id_str, tweet.created_at,tweet.text.encode("utf-8"),tweet.entities,tweet.retweet_count,tweet.favorite_count,tweet.in_reply_to_screen_name,tweet.lang]
        # for tweet in c]
        # with open('%s_retweets.csv' %  screen_name, 'a+') as f:
    	# 			writer = csv.writer(f)
    	# 			writer.writerows(outtweets)
