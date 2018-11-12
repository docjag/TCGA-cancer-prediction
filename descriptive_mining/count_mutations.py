import csv

mutation_dict = {}

with open('Full_List_sorted.csv','rb') as genecsvfile:
    thedata = csv.reader(genecsvfile)
    for row in thedata:
    	mutation = row[1]
    	if mutation == 'Silent':
    		print row[0]
    	mutation_dict[mutation] = mutation_dict.get(mutation, 0) + 1

with open('mutation_stats.csv','wb') as fhand:
	wr = csv.writer(fhand, quoting=csv.QUOTE_NONE)
	for keys, values in mutation_dict.items():
		wr.writerow([keys, values])
