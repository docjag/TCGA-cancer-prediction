#Author: Sohel Mahmud
#Date: 14-08-16
#Description:
#

import csv
import json

genes = []
result = []
data = {}

# Parsing data from the JSON file
with open('JSON_Sorted/ACC.json', 'r') as readfile:
    mydata = json.load(readfile)                                    # mydata is a dictionary
                                                                    # There is another variant: json.loads() for parsing JSON file    

# Read the CSV gene mutation record file
with open('sample_gene_mutation_record.csv','r') as fhand:
    heading = fhand.readline()                                      # Reading the first line from the file
    heading.rstrip()                                                # Removing the EOL character '\n'
    heading =  heading.split(',')                                   # Spliting the fields with ',' delimiter
    heading.pop(0)                                                  # Removing the first field UserID
    heading.pop(len(heading)-1)                                     # Removing the last field Mutation_type

# Reading each gene from the gene mutation record file 
# Comparing with the members of user-gene JSON file which contains the mutated genes of a particular user
for key, lst_of_dct in mydata.items():
    print len(lst_of_dct)
    for dct in lst_of_dct:
        patient = dct['userID']
        genes = sorted(list(set(dct['genes'])))
        result.append(patient)
        if patient == 'TCGA-OR-A5J1-01':
            print patient, genes
        
        print len(heading)
 
        for head in heading:
            if head in genes:
                result.append(1)
            else:
                result.append(0)

        result.append('ACC')

        print result
        with open('sample_gene_mutation_record.csv', 'a') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
            wr.writerow(result)
        result = []
