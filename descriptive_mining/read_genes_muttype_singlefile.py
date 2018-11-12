#Author: Sohel Mahmud
#Date: 10-09-16
#Description: Extracting the genes along with the variant classification
#             and variant types from a single file of a single user,
#			  and storing in a CSV file.

import csv
import pandas as pd

genes = []
genes.append(['HUGO_ID','Variant_Classification','Variant_type'])
silent_dict = {}

output = 'gene_variants_filtered.csv'

for line in open("sample.maf",'r'):
    line = line.rstrip()
    columns = line.split('\t')
    if len(columns) >= 2:
        #Skipping the column headers
        if columns[0] == 'Hugo_Symbol': continue
        '''
        if columns[8] == 'Silent': 
            silent_dict['Silent'] = silent_dict.get('Silent',0) + 1
            continue
        '''
        #Append multiple values in list
        genes.append([columns[0],columns[8], columns[9]])


#Writing in a CSV file by rows
with open(output, 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    for row in genes:
    	wr.writerow(row)

#Sorting the CSV file using Pandas Package
df = pd.read_csv(output)
df = df.sort_values(by='HUGO_ID')
df.to_csv('Full_List_sorted.csv', index=False)
