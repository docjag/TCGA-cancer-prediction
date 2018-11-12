#Author: Sohel Mahmud
#Date: 15-08-16
#Description:
#


import csv

silent_mut = {}
genes = ['#userID']

for line in open("TCGA-OR-A5J1-01.maf",'r'):
    line = line.rstrip()
    columns = line.split('\t')
    if len(columns) >= 2:
    	if columns[0] == 'Hugo_Symbol': continue
        if columns[8] == 'Silent':                                  # Filtering out the silent mutated genes
            silent_mut['Silent'] = silent_mut.get('Silent', 0) + 1
            continue
        genes.append(columns[0])

print len(genes)
print silent_mut['Silent']

genes = sorted(list(set(genes)))
genes.append('Mutation_type')

with open('sample_gene_mutation_record.csv', 'wb') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    wr.writerow(genes)
