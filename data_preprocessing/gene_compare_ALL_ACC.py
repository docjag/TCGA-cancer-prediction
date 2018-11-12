#Author: Sohel Mahmud
#Date: 05-10-16
#Description: Comparing the genes (7108)of ACC patients (90) with gene pool (22255) and creating a binary matrix
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
with open('All_gene_mutation_record.csv','r') as fhand:
    heading = fhand.readline()                                      # Reading the first line from the file
    heading.rstrip()                                                # Removing the EOL character '\n'
    heading =  heading.split(',')                                   # Spliting the fields with ',' delimiter
                                                                    # heading contains all ACC tumor genes (7108)
    heading.pop(0)                                                  # Removing the first field UserID
    heading.pop(len(heading)-1)                                     # Removing the last field Mutation_type

# Reading each gene from the gene mutation record file 
# Comparing with the members of user-gene JSON file which contains the mutated genes of a particular user
for key, lst_of_dct in mydata.items():
    print len(lst_of_dct)											# print the total number of patients for ACC tumor
    																# lst_of_dct is list of dictionaries(patients=90) from ACC.json
    for dct in lst_of_dct:											# dct is each dictionary(2 keys - patient ID and genes(list))
        patient = dct['userID']
        genes = sorted(list(set(dct['genes'])))
        
        result.append(patient)										# Appending the patient ID in the result list
        
        print len(heading)											# print the number of total genes (22255)
 
        for head in heading:
            if head in genes:										# Comparing the header genes with the ACC genes
                result.append(1)
            else:
                result.append(0)

        result.append('ACC')										# Appending the tumor name in the result list

        print result
        with open('All_gene_mutation_record.csv', 'a') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
            wr.writerow(result)
        result = []
