#Author: Sohel Mahmud
#Date: 15-08-16
#Description:
#


import csv

genes = []
result = []

#
for line in open("TCGA-OR-A5J1-01.maf",'r'):
    line = line.rstrip()
    columns = line.split('\t')
    if len(columns) >= 2:
        #print columns[0]
        if columns[0] <> 'Hugo_Symbol':
            genes.append(columns[0])

result.append('TCGA-OR-A5J1')

# Read the CSV gene mutation record file
with open('sample_gene_mutation_record2.csv','r') as fhand:
    heading = fhand.readline()                      # Reading the first line from the file
    
    heading.rstrip()                                # Removing the EOL character '\n'
    heading =  heading.split(',')                   # Spliting the fields with ',' delimiter
    
    heading.pop(0)                                  # Removing the first field UserID
    heading.pop(len(heading)-1)                     # Removing the last field Mutation_type
    
    # Reading each gene from the gene mutation record file
    # compare with the members of the list 'genes' which contains
    # the mutated genes of a particular user
    for head in heading:
        if head in genes:
            print 1
            result.append(1)
        else:
            print 0
            result.append(0)
    fhand.close()
                
result.append('ACC')
print result

with open('sample_gene_mutation_record2.csv', 'a') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
    wr.writerow(result)

