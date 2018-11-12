# @Author: Sohel Mahmud
# @Date: 09-10-16
# @Description: 

import csv
import os
from os import path
#import matplotlib.pyplot as plt

# Getting the path of the firebrowse directory one level above
unordered = os.getcwd() + '/tumors_all_mutations'

# List comprehension for extracting the names of the files in firebrowse directory
files = [x for x in os.listdir(unordered) if path.isfile(unordered + os.sep + x)]

files.sort()     

gene_lst = []

with open('ACC.csv', 'rb') as fhand:
	for line in fhand:
		line = line.rstrip()
		gene_lst.append(line.split(',')[0])

print '50 most frequently mutated genes of ACC'
print gene_lst

tumor_lst = ['genes'] + [file.split('.')[0] for file in files]


with open('test.csv','a') as fhand:
	test = csv.writer(fhand, quoting=csv.QUOTE_NONE)
	test.writerow(tumor_lst)

for file in files:
	file = os.getcwd() + os.sep + 'tumors_all_mutations/' + file
	print 'Tumor: ' + file.split('/')[5].split('.')[0]

	gene_pool = []
	with open(file,'rb') as read_me:
		for line in read_me:
			line = line.rstrip()
			gene_pool.append(line)

	gene_dict = {}
	for gene in gene_lst:
		gene_dict[gene] = gene_pool.count(gene)

	print len(gene_dict.keys())
	print gene_dict



#print gene_dict

'''
a = gene_dict.keys()
b = gene_dict.values()
c = range(1, len(a) + 1)
print c

fig, ax = plt.subplots()
ax.scatter(b,c)
for i, txt in enumerate(a):
	ax.annotate(txt, (c[i], b[i]))

plt.xticks(c,a)
plt.xlabel('50 Most frequent Genes')
plt.ylabel('Frequency')
plt.title('Distribution of frequent genes among the tumors')
plt.legend(loc='left')
plt.show()
'''