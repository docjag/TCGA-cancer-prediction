#Author: Sohel Mahmud
#Date: 15-08-16
#Description:
#


import json

genes = []

data = {}

for line in open("sample.maf",'r'):
    line = line.rstrip()
    columns = line.split('\t')
    if len(columns) >= 2:
        #print columns[0]
        if columns[0] == 'Hugo_Symbol': continue
        genes.append(columns[0])
        with open('genes_TCGA-OR-A5J1.txt', 'a') as fhand:
            fhand.write(columns[0] + '\n')
            fhand.close()
            
for gene in genes:
    print gene
