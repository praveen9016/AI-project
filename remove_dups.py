import csv
result = []

if __name__ == '__main__':
	i = 0	
	with open('dataset_users.csv','rb') as f:
		reader = csv.reader(f)
		for row in reader

			for e in row:
				try:
					with open('%s_followees.csv'%e,'rb') as d:
						getcs = csv.reader(d)
						for r in getcs
							print r
						gotl = r[:200]					
						i = i + 1
					
						result = result.append(list(set(gotl)))

				except:
					pass
	print result	
