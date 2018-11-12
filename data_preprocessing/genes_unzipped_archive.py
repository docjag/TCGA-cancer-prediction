#Author: Sohel Mahmud
#Date: 15-08-16
#Description:
#


import os
from os import path

# List comprehension for extracting the names of the files in firebrowse directory
files = [x for x in os.listdir('ACC') if path.isfile('ACC' + os.sep + x)]

files.sort()

gene_list =  list()

for myfile in files:
    if myfile == 'MANIFEST.txt': continue
    for line in open('ACC/' + myfile,'r'):
        line = line.rstrip()
        columns = line.split('\t')
        if len(columns) >= 2:
            print columns[0]
            if columns[0] == 'Hugo_Symbol': continue
            gene_list.append(columns[0])
            with open('dump_all_genes.txt', 'a') as fhand:
                fhand.write(columns[0] + '\n')
                fhand.close()
                
gene_list.sort()

for gene in gene_list:
    with open('dump_all_genes_sorted.txt', 'a') as fhand:
        fhand.write(gene + '\n')
    fhand.close()
            
